import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

def transform(img,kernel):
    # Lấy kích thước ảnh
    width, height = img.size

    # Duyệt qua từng pixel và thực hiện
    for y in range(height):
        for x in range(width):
            arr=[]
            # Tính giá trị mới
            for y1 in range(-int(kernel/2),int(round(kernel/2))):
                for x1 in range(-int(kernel/2),int(round(kernel/2))):
                    if(x+x1>=0 and y+y1>=0 and x+x1<width and y+y1<height):
                        arr.append(img.getpixel((x+x1, y+y1)))
                    else: arr.append(0)
            new_color = sorted(arr)[int(len(arr)/2)]
            # Đặt lại giá trị pixel mới
            img.putpixel((x, y), new_color)

    # Lưu hình ảnh mới
    return img

def plot(image_path,kernel=3):
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
    img = transform(img,kernel)

    # Hiển thị hình ảnh biến đổi
    plt.subplot(1, 2, 2)
    plt.title(f'Hình ảnh biến đổi kernel={kernel}x{kernel}')
    plt.imshow(img,cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

plot("trung vị.jpg",kernel=3)