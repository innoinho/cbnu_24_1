import pandas as pd

data = pd.read_excel('배전반_데이터_엑셀수정.xlsx')

# 최빈값 계산
mode_value = data['도어열림'].mode()[0]  # mode() 함수는 최빈값을 반환합니다. [0]은 최빈값 중 첫 번째 값을 의미합니다.

# 결측치를 최빈값으로 대체
data_filled_mode = data.fillna({'도어열림': mode_value})

# 최빈값 계산
mode_value = data['지진가속도센서값'].mode()[0]  # mode() 함수는 최빈값을 반환합니다. [0]은 최빈값 중 첫 번째 값을 의미합니다.

# 결측치를 최빈값으로 대체
data_filled_mode = data.fillna({'지진가속도센서값': mode_value})

data.isnull().sum()
