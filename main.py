import math
import struct
import numpy as np


file_width = 100
file_height = 100
file_size = 0
color_depth = 4
color_num = 32
file_offset = 54
max_t = 10 * np.pi
max_range = file_width // 2 + 1
min_range = - ((file_width // 2) - 1)


points = []
for t in np.arange(0, max_t + 0.1, 0.05):
    x = round(24.8 * (math.cos(t) + math.cos(6.2*t) / 6.2))
    y = round(24.8 * (math.sin(t) + math.sin(6.2*t) / 6.2))
    if [x, y] not in points:
        points.append([x, y])
        points.append([x, -y])


with open("graph.bmp", "wb") as file:
    # создаем блок BITMAPFILEHEADER
    file.write(struct.pack("<2ci2hi", b'B', b'M', file_size, 0, 0, file_offset))
    # создаем блок BITMAPINFOHEADER
    file.write(struct.pack("<3i2h6i", 40, file_width, file_height, 1, color_num, 0, file_size * color_depth, 0, 0, 0, 0))
    for y in range(min_range, max_range):
        for x in range(min_range, max_range):
            cords = [x, y]
            if cords in points:
                file.write(struct.pack("<i", 0))
            else:
                file.write(struct.pack("<i", 16777215))
