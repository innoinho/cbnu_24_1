import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # RandomForestRegressor 임포트 추가
from sklearn.metrics import mean_squared_error
import seaborn as sns

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

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 사용할 한글 폰트명을 설정(맑은고딕 선택 PC에 따라 나눔고딕이 인식이 안되어 변경)
plt.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시 마이너스 기호가 깨지는 것을 방지.

# 상관 행렬 히트맵 그리기
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", xticklabels=correlation_matrix.columns, yticklabels=correlation_matrix.columns)
plt.title('Correlation Matrix')
plt.show()
# 모델 활용
# 이후에는 학습된 모델을 활용하여 새로운 데이터에 대한 예측을 수행하고 결과를 분석할 수 있습니다.




