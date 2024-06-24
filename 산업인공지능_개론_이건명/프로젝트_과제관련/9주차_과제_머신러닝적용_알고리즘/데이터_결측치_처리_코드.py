import pandas as pd

data = pd.read_excel('배전반_데이터_엑셀수정.xlsx')

# 도어열림 열의 결측치 처리
door_mode_value = data['도어열림'].mode()[0]  # 도어열림 열의 최빈값 계산
data['도어열림'].fillna(door_mode_value, inplace=True)  # 도어열림 열의 결측치를 최빈값으로 대체

# 지진가속도센서값 열의 결측치 처리
sensor_mode_value = data['지진가속도센서값'].mode()[0]  # 지진가속도센서값 열의 최빈값 계산
data['지진가속도센서값'].fillna(sensor_mode_value, inplace=True)  # 지진가속도센서값 열의 결측치를 최빈값으로 대체

data.isnull().sum()

