from PIL import Image, ImageFilter

image = Image.new('RGB', (160, 90), (0, 0, 255))
for x in range(8, 31):
    for y in range(2, 36):
        image.putpixel((x, y), (128, 128, 128))

image.filter(ImageFilter.CONTOUR).show()