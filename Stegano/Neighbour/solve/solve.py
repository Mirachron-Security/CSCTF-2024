#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import cv2
import numpy as np

image = cv2.imread('out.png') 

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
background_color = np.bincount(gray_image.ravel()).argmax()
text_color = 255 - background_color
mask = gray_image != background_color

image_with_reversed_colors = image.copy()
image_with_reversed_colors[mask] = 255 - image_with_reversed_colors[mask]

cv2.imshow('Image with Reversed Colors', image_with_reversed_colors)

while True:
    key = cv2.waitKey(1)
    if key == 27 or cv2.getWindowProperty('Image with Reversed Colors', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()

outfile = 'flag.png'
cv2.imwrite(outfile, image_with_reversed_colors)
print(f'Image saved as {outfile}')
