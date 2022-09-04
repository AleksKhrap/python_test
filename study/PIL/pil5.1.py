from PIL import Image, ImageChops

img = Image.open('C:\\Users\\Alexandr\\Desktop\\3.jpg')
x, y = img.size
img = ImageChops.offset(img, x//2, 0)

'''или
im1 = img.crop((0, 0, x // 2, y))
im2 = img.crop((x // 2, 0, x, y))
img.paste(im2, (0, 0))
img.paste(im1, (x // 2, 0))
'''

img.show()
