from PIL import Image, ImageEnhance

img = Image.open("C:\\Users\\Alexandr\\Desktop\\2.jpg")

im = ImageEnhance.Brightness(img)

a = im.enhance(5)
b = ImageEnhance.Contrast(a)
b.enhance(5).show()
print("Номер автомобиля: О753КЕ 123\n3 красные машины")
