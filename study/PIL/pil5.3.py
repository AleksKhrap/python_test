from PIL import Image
import random

img = Image.open('C:\\Users\\Alexandr\\Desktop\\3.jpg')

n = int(input('Введите количество частей: '))
x, y = img.size

for i in range(n):
    r = random.randint(1, n - 1)

    im1 = img.crop((0, y // n * i, x, y // n * (i + 1)))
    im2 = img.crop((0, y // n * r, x, y // n * (r + 1)))

    img.paste(im1, (0, y // n * r, x, y // n * (r + 1)))
    img.paste(im2, (0, y // n * i, x, y // n * (i + 1)))

img.show()
