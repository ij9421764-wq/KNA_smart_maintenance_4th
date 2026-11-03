import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent

DATA_PATH = BASE / "data" / "09_ict_inspection_dirty.csv"
REPORT_PATH = BASE / "09_report.txt"
RUN_TO_STEP = 3

##################################################################################

# 실습 1
def read_csv_data(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            header = next(reader)   
            rows = list(reader)    

            return header, rows

    except FileNotFoundError:
        return [], []


##################################################################################

# 실습 2
def group_by_part(rows):
    
    by_part = {}
    dropped = 0

    for row in rows:
        if len(row) < 2:
            dropped += 1
            continue

        part = row[1].strip()

        if not part:
            dropped += 1
            continue

        if part not in by_part:
            by_part[part] = []

        by_part[part].append(row)

    return by_part, dropped

##################################################################################

# 실습 3
def calc_stats(rows, column=2):

    values = []

    for row in rows:
        try:
            values.append(float(row[column]))
        except (ValueError, IndexError):
            continue

    if not values:
        return None

    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "max": max(values),
        "min": min(values)
    }

##################################################################################

# 실습 4
def filter_valid_rows(rows, lo=0.0, hi=5000.0):

    valid = []
    rejected = []

    for line_no, row in enumerate(rows, start=2):
        try:
            inspection_id = row[0]

            value = float(row[2])

            if value < lo :
                raise ValueError("범위 미만")

            if value > hi:
                raise ValueError("범위 초과")

            valid.append(row)

        except IndexError:
            rejected.append((line_no, inspection_id, "열 부족"))

        except ValueError:
            rejected.append((line_no, inspection_id, "숫자 변환 실패"))

    return valid, rejected

##################################################################################

# 실습 5
def save_report(path, total_rows, valid_rows, rejected, stats):

    lines = []

    lines.append(f"전체 건수: {total_rows}")
    lines.append(f"유효 건수: {len(valid_rows)}")
    lines.append(f"제외 건수: {len(rejected)}")

    if stats:
        lines.append(f"평균: {stats['mean']:.2f}")
        lines.append(f"최대: {stats['max']:.2f}")
        lines.append(f"최소: {stats['min']:.2f}")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

##################################################################################

# 실습 6
def verify_part_counts(valid_rows):

    by_part, _ = group_by_part(valid_rows)

    check_sum = 0

    for part, part_rows in sorted(by_part.items()):
        stats = calc_stats(part_rows)

        count = stats["count"] if stats else 0
        check_sum += count

        print(f"{part}: {count}건")

    print(f"합계 {check_sum} / 유효 {len(valid_rows)} → {check_sum == len(valid_rows)}")
    
##################################################################################

def main():
    
    # 실습 1
    header, rows = read_csv_data(DATA_PATH)
    # print(f"[1단계] 헤더 {len(header)}개 / 데이터 {len(rows)}행")
    # if RUN_TO_STEP == 1:
    #     return
    
    ###########################################
    
    # 실습 2
    # by_part, dropped = group_by_part(rows)
    
    # print(f"[2단계] 부품 {', '.join(sorted(by_part.keys()))} {len(by_part)}종 / 부품명 누락 {dropped}행")
    # if RUN_TO_STEP == 2:
    #     return
    
    ###########################################
    
    # 실습 3
    # before = calc_stats(rows, 2)
    # print(f"[3단계] 범위 검증 전 통계: 숫자 : {before['count']}건, 평균 : {before['mean']}, 최대 : {before['max']}, 최소 : {before['min']}")
    # if RUN_TO_STEP == 3:
    #     return
    
    ###########################################
    
    # 실습 4
    valid, rejected = filter_valid_rows(rows)
    after = calc_stats(valid, 2)
    # print(f"[4단계] 유효 {len(valid)}건 / 제외 {len(rejected)}건")
    
    # for item in rejected:
    #     print("    제외:", item)

    # if RUN_TO_STEP == 4:
    #     return
    
    ###########################################
    
    # 실습 5
    save_report(REPORT_PATH, len(rows), valid, rejected, after)
    # print(f"[5단계] 리포트 생성: {REPORT_PATH.name}")
    # if RUN_TO_STEP == 5:
    #     return
    
    ###########################################

    # 실습 6
    verify_part_counts(valid)
    
if __name__ == "__main__":
    main()
