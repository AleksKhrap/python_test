from PIL import Image, ImageDraw

size = 650
img = Image.new('RGB', (size, size), 'black')
draw = ImageDraw.Draw(img)

draw.polygon(((0, 0), (0, size), (size//2, size//2)), (255, 255, 0))
draw.polygon(((size, 0), (size, size), (size//2, size//2)), (255, 20, 147))

img.show()
