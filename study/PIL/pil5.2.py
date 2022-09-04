from PIL import Image

img = Image.open('C:\\Users\\Alexandr\\Desktop\\3.jpg')
pixels = img.load()
x, y = img.size

im1 = img.crop((0, 0, x // 2, y // 2)).rotate(180)
im2 = img.crop((x // 2, y // 2, x, y)).rotate(180)
img.paste(im2, (0, 0))
img.paste(im1, (x // 2, y // 2))

img.show()
