from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (550, 600), 'white')
draw = ImageDraw.Draw(img)
text = "Khrapov Alexandr Alexandrovich"
font = ImageFont.truetype('arial.ttf', size=30)

draw.text((50, 200), text, font=font, fill='#1C0606')
draw.rectangle((50, 250, 105, 350), fill='yellow', outline=(0, 0, 0))
draw.rectangle((105, 250, 160, 350), fill='blue', outline=(0, 0, 0))

draw.rectangle((210, 250, 265, 350), fill='white', outline=(0, 0, 0))
draw.polygon(((265, 250), (320, 250), (292.5, 300), (320, 350), (265, 350)), fill='blue', outline=(0, 0, 0))

draw.rectangle((370, 250, 425, 350), fill='white', outline=(0, 0, 0))
draw.polygon(((425, 250), (480, 250), (452.5, 300), (480, 350), (425, 350)), fill='blue', outline=(0, 0, 0))

img.show()
