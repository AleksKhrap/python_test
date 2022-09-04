from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

img = Image.open("C:\\Users\\Alexandr\\Desktop\\Mustang.jpg")

img = img.filter(ImageFilter.DETAIL)
plt.figure()
x = list(range(0, len(img.histogram())))
plt.bar(x, img.histogram(), edgecolor='deeppink')

print("Улучшает качество (деталлизированность) изображения")
img.show()
plt.show()
