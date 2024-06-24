import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt

# GPU 사용 설정
physical_devices = tf.config.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# 데이터 전처리 및 증강 설정
train_datagen = ImageDataGenerator(
    rescale=1./255, # 픽셀 값을 0과 1 사이로 조정
    shear_range=0.2, # 이미지 증강 - 층 기울이기
    zoom_range=0.2, # 이미지 증강 - 확대 축소
    horizontal_flip=True, # 이미지 증강 - 뒤집기
    validation_split=0.2  # 학습 데이터 중 20%를 검증 데이터로 사용
)

# 학습 데이터와 검증 데이터 로드
training_set = train_datagen.flow_from_directory(
    'C:/cnn', # 학습 데이터가 저장된 디렉토리 경로
    target_size=(64, 64), # 모든 이미지를 64x64 크기로 조정
    batch_size=32, # 배치 크기 설정
    class_mode='categorical', # 클래스 모드를 카테고리로 설정 (다중 클래스 분류)
    classes=['blocks', 'clay', 'gardenia'], # 클래스 이름 지정
    subset='training'  # 학습 데이터 설정
)

validation_set = train_datagen.flow_from_directory(
    'C:/cnn', # 검증 데이터가 저장된 디렉토리 경로
    target_size=(64, 64), # 모든 이미지를 64x64 크기로 조정
    batch_size=32, # 배치 크기 설정
    class_mode='categorical', # 클래스 모드를 카테고리로 설정 (다중 클래스 분류)
    classes=['blocks', 'clay', 'gardenia'], # 클래스 이름 지정
    subset='validation'  # 검증 데이터 설정
)

# 모델 초기화
model = Sequential()

# 첫 번째 합성곱 층 추가
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu')) # 32개의 3x3 필터, ReLU 활성화 함수
model.add(MaxPooling2D(pool_size=(2, 2))) # 2x2 풀링 윈도우

# 두 번째 합성곱 층 추가
model.add(Conv2D(32, (3, 3), activation='relu')) # 32개의 3x3 필터, ReLU 활성화 함수
model.add(MaxPooling2D(pool_size=(2, 2))) # 2x2 풀링 윈도우

# 세 번째 합성곱 층 추가
model.add(Conv2D(64, (3, 3), activation='relu')) # 64개의 3x3 필터, ReLU 활성화 함수
model.add(MaxPooling2D(pool_size=(2, 2))) # 2x2 풀링 윈도우

# 평탄화 층 추가
model.add(Flatten()) # 2D 특징 맵을 1D 벡터로 변환

# 첫 번째 완전 연결 층 추가
model.add(Dense(units=64, activation='relu')) # 64개의 유닛, ReLU 활성화 함수
model.add(Dropout(0.5)) # 드롭아웃 비율 0.5

# 두 번째 완전 연결 층 추가
model.add(Dense(units=64, activation='relu')) # 64개의 유닛, ReLU 활성화 함수
model.add(Dropout(0.5)) # 드롭아웃 비율 0.5

# 출력 층 추가
model.add(Dense(units=3, activation='softmax')) # 3개의 유닛, Softmax 활성화 함수

# 모델 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) # Adam 옵티마이저, categorical crossentropy 손실 함수, 정확도 메트릭

# 모델 요약 출력
model.summary() # 모델 구조 요약 출력

# 모델 학습
history = model.fit(
    training_set, # 학습 데이터셋
    epochs=20, # 20번의 에포크 동안 학습
    validation_data=validation_set # 검증 데이터셋
)

# 모델 저장
model.save('C:/cnn/my_model.h5') # 모델을 'my_model.h5' 파일로 저장

# 학습 결과 출력
print("Training Accuracy:", history.history['accuracy'][-1]) # 마지막 에포크의 학습 정확도 출력
print("Validation Accuracy:", history.history['val_accuracy'][-1]) # 마지막 에포크의 검증 정확도 출력

# 테스트 데이터로 모델 평가
test_loss, test_accuracy = model.evaluate(validation_set) # 검증 데이터셋으로 모델 평가
print("Test Loss:", test_loss) # 테스트 손실 출력
print("Test Accuracy:", test_accuracy) # 테스트 정확도 출력

# 정확도 그래프 출력
plt.plot(history.history['accuracy'], label='Training Accuracy') # 학습 정확도 그래프
plt.plot(history.history['val_accuracy'], label='Validation Accuracy') # 검증 정확도 그래프
plt.xlabel('Epoch') # x축 라벨
plt.ylabel('Accuracy') # y축 라벨
plt.title('Training and Validation Accuracy') # 그래프 제목
plt.legend() # 범례 추가
plt.show() # 그래프 출력

# 손실 그래프 출력
plt.plot(history.history['loss'], label='Training Loss') # 학습 손실 그래프
plt.plot(history.history['val_loss'], label='Validation Loss') # 검증 손실 그래프
plt.xlabel('Epoch') # x축 라벨
plt.ylabel('Loss') # y축 라벨
plt.title('Training and Validation Loss') # 그래프 제목
plt.legend() # 범례 추가
plt.show() # 그래프 출력

# 저장된 모델 불러오기
loaded_model = tf.keras.models.load_model('C:/cnn/my_model.h5') # 저장된 모델 불러오기

# 불러온 모델로 테스트 데이터 평가
test_loss, test_accuracy = loaded_model.evaluate(validation_set) # 검증 데이터셋으로 모델 평가
print("Loaded Model Test Loss:", test_loss) # 불러온 모델의 테스트 손실 출력
print("Loaded Model Test Accuracy:", test_accuracy) # 불러온 모델의 테스트 정확도 출력
