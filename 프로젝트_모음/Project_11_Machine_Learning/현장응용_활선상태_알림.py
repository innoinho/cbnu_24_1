import pandas as pd

# 엑셀 파일에서 데이터 불러오기
data = pd.read_excel('배전반_데이터_엑셀수정.xlsx')

# 도어가 연속해서 열렸는지 확인하는 함수
def check_consecutive_door_opening(data, start_index, consecutive_count):
    for i in range(start_index, start_index + consecutive_count):
        if i >= len(data):
            return False
        if data.iloc[i]['도어열림'] not in ['F', 'M', 'B', 'sensor']:
            return False
    return True

# 도어가 열렸을 때의 조건 확인 및 알림 기록
def check_door_condition(data, start_index):
    consecutive_count = 10  # 연속된 도어열림 상태를 확인할 횟수
    if check_consecutive_door_opening(data, start_index, consecutive_count):
        for i in range(start_index, start_index + consecutive_count):
            row = data.iloc[i]
            if row['온도'] >= 29 or row['습도'] >= 65:
                if row['온도'] >= 29:
                    print(f"도어가 연속해서 열렸으며 온도가 29 이상입니다. (행: {i+1})")
                if row['습도'] >= 65:
                    print(f"도어가 연속해서 열렸으며 습도가 65 이상입니다. (행: {i+1})")
        return True
    return False

# 활선상태가 RST 중 어떤 값인지 확인하고 도어가 열렸을 때 위험신호로 감지하는 함수
def check_power_condition(data, start_index):
    consecutive_count = 10  # 연속된 도어열림 상태를 확인할 횟수
    if check_consecutive_door_opening(data, start_index, consecutive_count):
        for i in range(start_index, start_index + consecutive_count):
            row = data.iloc[i]
            if 'R' in row['활선상태'] or 'S' in row['활선상태'] or 'T' in row['활선상태']:
                print(f"도어가 연속해서 열렸으며 RST중 하나이상 활선상태가 입니다. (행: {i+1})")
        return True
    return False

# 알림 횟수를 기록할 변수
alert_count = 0

# 데이터 프레임의 각 행에 대해 조건을 검사하고 알림을 줌
for i in range(len(data) - 9):  # 10개의 연속된 행에 대해 확인
    if check_door_condition(data, i):
        alert_count += 1
    if check_power_condition(data, i):
        alert_count += 1

print("알림을 준 횟수:", alert_count)
