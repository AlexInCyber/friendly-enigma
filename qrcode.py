import numpy as np
from PIL import Image

img = Image.open('image.png')
pixels = list(img.getdata())
new_pixels = []

# extragem bitii LSB si reconstruim alb/negru
for pixel_data in pixels:
    dark_white = False
    for v in pixel_data[:-1]:
        dark_white = dark_white or (v % 2 == 1)
    new_pixels.append(0 if dark_white else 0xff)

# cream noua imagine
img = Image.new('RGBA', img.size, 255)
data = img.load()

cnt = 0
for x in range(img.size[0]):
    for y in range(img.size[1]):
        v = new_pixels[cnt]
        data[x, y] = (v, v, v, 255)
        cnt += 1

# aplicam masca pentru claritate
def setSquare(start_x, start_y, color):
    for x in range(start_x, start_x + 5):
        for y in range(start_y, start_y + 5):
            data[x, y] = (color, color, color, 255)

for square_start_x in range(2, img.size[0] - 5, 5):
    for square_start_y in range(2, img.size[1] - 5, 5):
        dark_white_squares = 0
        for x in range(square_start_x, square_start_x + 5):
            for y in range(square_start_y, square_start_y + 5):
                if data[x, y][0] == 0:
                    dark_white_squares += 1
        if dark_white_squares > 12:
            setSquare(square_start_x, square_start_y, 0)
        else:
            setSquare(square_start_x, square_start_y, 255)

img.save('qr.png')
