# 필요한 라이브러리 import
import pandas as pd

# 데이터 파일 불러오기
data = pd.read_csv("data.csv")

# 문자열을 포함한 열 제거
data = data.drop(columns=["column_with_strings"])

# 결측치 처리
data.dropna(inplace=True)

# 데이터 정규화
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# 특성 선택
X = scaled_data.drop(columns=["target_column"])
y = scaled_data["target_column"]

# 모델 선택
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

# 모델 학습
model.fit(X, y)

# 모델 평가
from sklearn.metrics import accuracy_score
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# 배포할 때 사용할 모델 저장
import joblib
joblib.dump(model, "model.pkl")


print(data.columns)
