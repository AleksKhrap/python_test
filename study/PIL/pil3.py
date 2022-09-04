from PIL import Image, ImageDraw

a = int(input('Введите размер рисунка:'))
b = int(input('Введите количество эллипсов:'))

img = Image.new('RGB', (a + 5, a + 5), 'white')
draw = ImageDraw.Draw(img)


def ellipse(x, y):
    for i in range(b):
        draw.ellipse((((x / y) / 2 * i), 0, x - (x / y) / 2 * i, x), outline='#FF1493')
        draw.ellipse((0, ((x / y) / 2 * i), x, x - (x / y) / 2 * i), outline='#FF1493')
    img.show()


ellipse(a, b)
