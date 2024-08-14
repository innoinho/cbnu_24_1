import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor  
from sklearn.metrics import mean_squared_error
import seaborn as sns

# 데이터셋 불러오기
data = pd.read_excel('배전반_데이터_엑셀수정.xlsx')

# 도어열림 열의 결측치 처리
door_mode_value = data['도어열림'].mode()[0]  
data['도어열림'].fillna(door_mode_value, inplace=True)  

# 지진가속도센서값 열의 결측치 처리
sensor_mode_value = data['지진가속도센서값'].mode()[0]  
data['지진가속도센서값'].fillna(sensor_mode_value, inplace=True)  

# 독립 변수와 종속 변수 분리
X = data[['전압1', '전압2', '전압3', '전류1', '전류2', '전류3']]
y = data['최대전력']

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 머신러닝 모델 선택 및 학습(RandomForestRegressor)
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)  
model_rf.fit(X_train, y_train)  

# 모델 평가
y_pred_rf = model_rf.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
print('Mean Squared Error (RandomForest):', mse_rf)

# 교차 검증(RandomForest)
scores_rf = cross_val_score(model_rf, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
print("Cross-validated MSE (RandomForest):", -scores_rf.mean())

# 상관 행렬 계산
correlation_matrix = X.corr()

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  
plt.rcParams['axes.unicode_minus'] = False  

# 상관 행렬 히트맵 그리기
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", xticklabels=correlation_matrix.columns, yticklabels=correlation_matrix.columns)
plt.title('Correlation Matrix')
plt.show()

# 예측값과 실제값의 차이 계산
percentage_diff = ((y_pred_rf - y_test) / y_test) * 100

# NaN 값을 제외하고 퍼센트 오차 출력
percentage_diff.dropna(inplace=True)
print("Percentage Difference:", percentage_diff)

