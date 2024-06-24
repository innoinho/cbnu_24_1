import sys
import os
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(os.pardir)
from tensorflow.keras.datasets import mnist

# Load MNIST data
(x_train, t_train), (x_test, t_test) = mnist.load_data()

# Print shapes of the loaded data
print("Training data shape:", x_train.shape)
print("Training labels shape:", t_train.shape)
print("Test data shape:", x_test.shape)
print("Test labels shape:", t_test.shape)

# Display sample images
num_images_to_display = 5
for i in range(num_images_to_display):
    plt.subplot(1, num_images_to_display, i+1)
    plt.imshow(x_train[i], cmap='gray')  # Display the image in grayscale
    plt.title("Label: {}".format(t_train[i]))
    plt.axis('off')  # Turn off axis
plt.show()

