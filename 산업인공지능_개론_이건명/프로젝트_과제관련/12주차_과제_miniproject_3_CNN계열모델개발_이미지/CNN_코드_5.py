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
    shear_range=0.2, #이미지 증강 - 층 기울이기
    zoom_range=0.2,  #이미지 증강 - 확대 축소
    horizontal_flip=True, #이미지 증강 - 뒤집기
    validation_split=0.2  # 학습 데이터 중 20%를 검증 데이터로 사용
)

# 학습 데이터와 검증 데이터 로드
training_set = train_datagen.flow_from_directory(
    'C:/cnn',
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical',
    classes=['blocks', 'clay', 'gardenia'],
    subset='training'  # 학습 데이터 설정
)

validation_set = train_datagen.flow_from_directory(
    'C:/cnn',
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical',
    classes=['blocks', 'clay', 'gardenia'],
    subset='validation'  # 검증 데이터 설정
)

# 모델 초기화
model = Sequential()

# 첫 번째 합성곱 층 추가
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 두 번째 합성곱 층 추가
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 세 번째 합성곱 층 추가
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 평탄화 층 추가
model.add(Flatten())

# 첫 번째 완전 연결 층 추가
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(0.5))

# 두 번째 완전 연결 층 추가
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(0.5))

# 출력 층 추가
model.add(Dense(units=3, activation='softmax'))

# 모델 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 모델 학습
history = model.fit(
    training_set,
    epochs=20,
    validation_data=validation_set
)

# 모델 저장
model.save('C:/cnn/my_model5.h5')

# 학습 결과 출력
print("Training Accuracy:", history.history['accuracy'][-1])
print("Validation Accuracy:", history.history['val_accuracy'][-1])

# 저장된 모델 불러오기
loaded_model = tf.keras.models.load_model('C:/cnn/my_model5.h5')

# 불러온 모델로 테스트 데이터 평가
test_loss, test_accuracy = loaded_model.evaluate(validation_set)
print("Loaded Model Test Loss:", test_loss)
print("Loaded Model Test Accuracy:", test_accuracy)

# 학습 및 검증 정확도 그래프 출력
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

# 학습 및 검증 손실 그래프 출력
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()

plt.tight_layout()
plt.show()

