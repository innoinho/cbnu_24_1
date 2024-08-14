import pandas as pd

data = pd.read_csv("data1.csv")

print(data.head())  # 데이터 일부 출력
print(data.info())  # 데이터 정보 출력
print(data.describe())  # 데이터 통계 정보 출력

# 결측치 처리
data["es_door"].fillna("Unknown", inplace=True)
data["es_wave"].fillna("Unknown", inplace=True)

# 범주형 데이터 처리 (더미 변수 생성)
data = pd.get_dummies(data, columns=["es_door", "es_wave", "es_alive"], drop_first=True)

# 날짜 데이터 처리
data["es_date"] = pd.to_datetime(data["es_date"])

# 데이터 스케일링 (예시: Min-Max 스케일링)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data.drop(columns=["es_date"]))

# 데이터 분할
X = scaled_data[:, 1:]  # es_no 열 제외한 모든 특성
y = scaled_data[:, 0]   # es_no 열 (타겟 변수)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

