#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import cv2
import numpy as np

background_color = (255, 255, 255)  
text_color = (254, 254, 254)  

M = 5000
N = 5000
white_image = np.zeros((M, N, 3), dtype=np.uint8)
white_image[:] = background_color

flag = 'CSCTF{an07h3r_3mp7y_1m4g3}'

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.4
font_thickness = 1
text_size = cv2.getTextSize(flag, font, font_scale, font_thickness)[0]
text_x = (N - text_size[0]) // 2
text_y = (M - text_size[1]) * 9 // 10
text_position = (text_x, text_y)

image_with_text = cv2.putText(white_image.copy(), flag, text_position, font, font_scale, text_color, font_thickness)

cv2.imshow('Image with Text', image_with_text)

while True:
    key = cv2.waitKey(1)
    if key == 27 or cv2.getWindowProperty('Image with Text', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()

outfile = 'out.png'
cv2.imwrite(outfile, image_with_text)
print(f'Image saved as {outfile}')
