# 주식 시장 데이터가 아니지만, 예시로 랜덤 데이터를 생성하여 활용하겠습니다.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  
from sklearn.metrics import mean_squared_error

# 랜덤 주식 데이터 생성
np.random.seed(42)
num_samples = 1000
data = pd.DataFrame({
    'Price': np.random.normal(100, 20, num_samples),
    'Volume': np.random.randint(10000, 1000000, num_samples),
    'MarketCap': np.random.randint(1000000, 10000000, num_samples)
})

# 독립 변수와 종속 변수 분리
X = data[['Volume', 'MarketCap']]
y = data['Price']

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 머신러닝 모델 선택 및 학습(RandomForestRegressor)
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)  
model_rf.fit(X_train, y_train)  

# 모델 평가
y_pred_rf = model_rf.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
print('Mean Squared Error (RandomForest):', mse_rf)

# 상관 행렬 계산
correlation_matrix = X.corr()

# 상관 행렬 히트맵 그리기
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", xticklabels=correlation_matrix.columns, yticklabels=correlation_matrix.columns)
plt.title('Correlation Matrix')
plt.show()

# 예측값과 실제값의 비교 그래프
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_rf, alpha=0.5)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs. Predicted Prices')
plt.show()

