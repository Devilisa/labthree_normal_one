import math
import struct
import numpy as np


File_Width = 100
File_Height = 100
File_Size = 0
Color_depth = 4
Color_num = 32
File_Offset = 54
Max_t = 10 * np.pi
Max_range = File_Width // 2 + 1
Min_range = - ((File_Width // 2) - 1)

points = []
for t in np.arange(0, Max_t + 0.1, 0.05):
    x = round(24.8 * (math.cos(t) + math.cos(6.2 * t) / 6.2))
    # x^2 + y^2 = 631,04 + 198,4 * cos(7,2t) отсюда выразим y через x
    y = round(((631.04 + 198.4 * math.cos(7.2 * t) - x ** 2) ** 0.5).real)
    if [x, y] not in points:
        points.append([x, y])
        points.append([x, -y])


with open("graph.bmp", "wb") as file:
    # создаем блок BITMAPFILEHEADER
    file.write(struct.pack("<2ci2hi", b'B', b'M', File_Size, 0, 0, File_Offset))
    # создаем блок BITMAPINFOHEADER
    file.write(struct.pack("<3i2h6i", 40, File_Width, File_Height, 1, Color_num, 0, File_Size*Color_depth, 0, 0, 0, 0))
    for y in range(Min_range, Max_range):
        for x in range(Min_range, Max_range):
            cords = [x, y]
            if cords in points:
                file.write(struct.pack("<i", 0))
            else:
                file.write(struct.pack("<i", 16777215))
