from PIL import Image
import random

img = Image.open('C:\\Users\\Alexandr\\Desktop\\3.jpg')
x, y = img.size

n = int(input('Введите количество частей: '))

for i in range(n):
    x1 = random.randrange(0, x - 50, 50)
    y1 = random.randrange(0, y - 50, 50)
    x2 = random.randrange(0, x - 50, 50)
    y2 = random.randrange(0, y - 50, 50)

    im1 = img.crop((x1, y1, x1 + 50, y1 + 50)).rotate(random.randrange(0, 270, 90))

    img.paste(im1, (x2, y2, x2 + 50, y2 + 50))

img.show()
