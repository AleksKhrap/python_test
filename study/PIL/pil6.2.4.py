from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

img = Image.open("C:\\Users\\Alexandr\\Desktop\\Mustang.jpg")

img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
plt.figure()
x = list(range(0, len(img.histogram())))
plt.bar(x, img.histogram(), edgecolor='deeppink')

print("То же, что и предыдущий, только все становится еще более явным (сильным)")
img.show()
plt.show()
