import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 데이터셋 불러오기
data = pd.read_excel('배전반_데이터_엑셀수정.xlsx')

# 도어열림 열의 결측치 처리
door_mode_value = data['도어열림'].mode()[0]  # 도어열림 열의 최빈값 계산
data['도어열림'].fillna(door_mode_value, inplace=True)  # 도어열림 열의 결측치를 최빈값으로 대체

# 지진가속도센서값 열의 결측치 처리
sensor_mode_value = data['지진가속도센서값'].mode()[0]  # 지진가속도센서값 열의 최빈값 계산
data['지진가속도센서값'].fillna(sensor_mode_value, inplace=True)  # 지진가속도센서값 열의 결측치를 최빈값으로 대체

# 데이터 요약 통계 출력
summary_stats = data.describe()
print(summary_stats)

# 숫자 열만 선택하여 상관 행렬 계산
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# 상관 행렬 계산
correlation_matrix = numeric_data.corr()
print(correlation_matrix)

# 온도와 습도 간의 산점도 그리기
plt.scatter(data['온도'], data['습도'])
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Temperature vs Humidity')
plt.show()

# 독립 변수와 종속 변수 분리
X = data[['온도', '습도', '전압1', '전압2', '전압3', '전류1', '전류2', '전류3', '역률', '고조파불평형률1', '고조파불평형률2', '고조파불평형률3']]
y = data['최대전력']


# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 머신러닝 모델 선택 및 학습
model = RandomForestRegressor(n_estimators=100, random_state=42)  # RandomForestRegressor 모델 선택
model.fit(X_train, y_train)  # 모델 학습

# 모델 평가
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# 모델 활용
# 이후에는 학습된 모델을 활용하여 새로운 데이터에 대한 예측을 수행하고 결과를 분석할 수 있습니다.









