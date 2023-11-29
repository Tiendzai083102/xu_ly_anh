import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

input_image=Image.open("gian.jpg").convert('1')
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
        if(image[i,j-1]==1 or image[i-1,j]==1 or image[i,j]==1 or image[i+1,j]==1 or image[i,j+1]==1):
            result[i,j]=1

plt.imshow(input_image,cmap='gray')
plt.show()

plt.imshow(result,cmap='gray')

plt.show()