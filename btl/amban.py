import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

def negative_transform(img):
    try:
        # Lấy kích thước ảnh
        width, height = img.size

        # Duyệt qua từng pixel và thực hiện phép biến đổi âm bản đối
        for y in range(height):
            for x in range(width):
                # Lấy giá trị pixel
                current_color = img.getpixel((x, y))

                # Tính giá trị âm bản đối
                new_color = tuple(255 - value for value in current_color)

                # Đặt lại giá trị pixel mới
                img.putpixel((x, y), new_color)

        # Lưu hình ảnh mới
        return img
    
    except Exception as e:
        print(f"Lỗi: {e}")

def plot(image_path):
    try:
        # Đọc hình ảnh
        img = Image.open(image_path)

        # Hiển thị hình ảnh ban đầu
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.title('Hình ảnh ban đầu')
        plt.imshow(img)
        plt.axis('off')

        # Thực hiện phép biến đổi âm bản đối
        img = negative_transform(img)

        # Hiển thị hình ảnh biến đổi
        plt.subplot(1, 2, 2)
        plt.title('Hình ảnh biến đổi âm bản đối')
        plt.imshow(img)
        plt.axis('off')

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Lỗi: {e}")

# Thực hiện phép biến đổi âm bản đối và hiển thị hình ảnh
plot("âm bản.jpg")