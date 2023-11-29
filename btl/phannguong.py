import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

def transform(img):
    try:
        # Lấy kích thước ảnh
        width, height = img.size

        # Duyệt qua từng pixel và thực hiện phân ngưỡng
        for y in range(height):
            for x in range(width):
                # Lấy giá trị pixel
                current_color = img.getpixel((x, y))

                # Tính giá trị ngưỡng
                new_color = tuple(0 if value <= 50 else 255 for value in current_color)


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

        # Thực hiện phép biến đổi
        img = transform(img)

        # Hiển thị hình ảnh biến đổi
        plt.subplot(1, 2, 2)
        plt.title('Hình ảnh biến đổi')
        plt.imshow(img)
        plt.axis('off')

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Lỗi: {e}")

plot("phân ngưỡng.jpg")