from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

input_image=Image.open("phân ngưỡng.jpg").convert('L')
grayscale_image = np.array(input_image)

Laplacian = np.array([[0.0, 1.0, 0.0], [1.0, -4.0, 1.0], [0.0, 1.0, 0.0]])
[rows, columns] = np.shape(grayscale_image)
Laplacian_filtered_image = np.zeros(shape=(rows, columns))

for i in range(rows - 2):
    for j in range(columns - 2):
        Laplacian_filtered_image[i + 1, j + 1] = np.sum(np.multiply(Laplacian, grayscale_image[i:i + 3, j:j + 3]))

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Hình ảnh ban đầu')
plt.imshow(input_image,cmap='gray')
plt.axis('off')

# Hiển thị hình ảnh biến đổi
plt.subplot(1, 2, 2)
plt.title(f'Hình ảnh biến đổi kernel=3x3')
plt.imshow(Laplacian_filtered_image,cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()