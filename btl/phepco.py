import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

input_image=Image.open("co.jpg").convert('1')
width, height = input_image.size

# Kernel
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]])

# Ảnh đen trắng (một ma trận 2D)
image = np.array(input_image)
[rows, columns] = np.shape(image)
result = np.zeros(shape=(rows, columns))

for i in range(1,height-2):
    for j in range(1,width-2):
        if(image[i,j-1]==1 and image[i-1,j]==1 and image[i,j]==1 and image[i+1,j]==1 and image[i,j+1]==1):
            result[i,j]=1

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Hình ảnh ban đầu')
plt.imshow(input_image,cmap='gray')
plt.axis('off')

# Hiển thị hình ảnh biến đổi
plt.subplot(1, 2, 2)
plt.title(f'Hình ảnh biến đổi kernel=3x3')
plt.imshow(result,cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()