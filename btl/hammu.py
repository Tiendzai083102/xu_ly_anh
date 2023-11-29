import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

def transform(img,c,mu):
    # Lấy kích thước ảnh
    width, height = img.size

    # Duyệt qua từng pixel và thực hiện
    for y in range(height):
        for x in range(width):
            # Lấy giá trị pixel
            current_color = img.getpixel((x, y))

            # Tính giá trị mới
            new_color = round(c*(current_color**mu))

            # Đặt lại giá trị pixel mới
            img.putpixel((x, y), new_color)

    # Lưu hình ảnh mới
    return img

def plot(image_path,c=1,y=0.6):
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
    img = transform(img,c,y)

    # Hiển thị hình ảnh biến đổi
    plt.subplot(1, 2, 2)
    plt.title('Hình ảnh biến đổi')
    plt.imshow(img,cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

plot("hàm mũ.jpg", c=1,y=0.4)