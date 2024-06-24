import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np

# 이미지 로드
img = imread('inho.jpg')

# 이미지를 오른쪽으로 90도 회전
img_rotated = np.rot90(img, k=-1)

# 이미지 표시
plt.imshow(img_rotated)
plt.show()
