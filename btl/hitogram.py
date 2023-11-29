import cv2
import matplotlib.pyplot as plt
import collections
from PIL import Image
import numpy as np

def transform(img):
    # Lấy kích thước ảnh
    width, height = img.size
    
    pixel_frequency = {}
    
    # Đếm tần suất xuất hiện của từng giá trị điểm ảnh
    for y in range(height):
        for x in range(width):
            pixel_value = img.getpixel((x, y))
            if pixel_value in pixel_frequency:
                pixel_frequency[pixel_value] += 1
            else:
                pixel_frequency[pixel_value] = 1
    key_sorted=sorted(pixel_frequency.keys())
    tmp = 0
    for key in key_sorted:
        tmp += 255*(pixel_frequency[key]/(width*height))
        pixel_frequency[key]=round(tmp)
        
    for y in range(height):
        for x in range(width):
            pixel_value = img.getpixel((x, y))
            
            img.putpixel((x, y), pixel_frequency[pixel_value])

    return img

def plot(image_path):
    # Đọc hình ảnh
    img = Image.open(image_path)
    img = img.convert('L')

    # Hiển thị hình ảnh ban đầu
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.title('Hình ảnh ban đầu')
    plt.imshow(img,cmap='gray')
    plt.axis('off')

    # Thực hiện phép biến đổi
    img = transform(img)

    # Hiển thị hình ảnh biến đổi
    plt.subplot(1, 2, 2)
    plt.title('Hình ảnh biến đổi')
    plt.imshow(img,cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

plot("histogram.jpg")