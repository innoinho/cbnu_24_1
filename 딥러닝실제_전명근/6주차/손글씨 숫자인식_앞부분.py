import sys
import os
sys.path.append(os.pardir)
from tensorflow.keras.datasets import mnist

(x_train, t_train), (x_test, t_test) = mnist.load_data()

print("Training data shape:", x_train.shape)
print("Training labels shape:", t_train.shape)
print("Test data shape:", x_test.shape)
print("Test labels shape:", t_test.shape)


import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

# MNIST 데이터셋 로드
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 첫 번째 이미지 표시
plt.imshow(train_images[0], cmap='gray')
plt.title(f"Label: {train_labels[0]}")
plt.axis('off')
plt.show()
