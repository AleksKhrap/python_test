from PIL import Image

size = 10
img = Image.new('L', (size, size), 'white')

pixels = img.load()

for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            pixels[i, j] = 255
        else:
            pixels[i, j] = 0
        if i == j:
            pixels[i, j] = 125

img.resize((50*size, 50*size), Image.NEAREST).show()
