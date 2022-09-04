from PIL import Image, ImageDraw

img = Image.new('RGB', (600, 600), 'white')
draw = ImageDraw.Draw(img)
x, y = img.size

a = int(input('Введите сторону квадрата: '))
b = int(input('Введите количество квадратов: '))
c = float(input('Введите коэффициент масштабирования: '))


def rectangle(d, e, f):
    for i in range(e):
        draw.rectangle((x / 2 - d / 2, y / 2 - d / 2, x / 2 + d / 2, y / 2 + d / 2), outline='#FF1493')
        d *= f
    img.show()


rectangle(a, b, c)
