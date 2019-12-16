# ch8/example2.py

import cv2

im = cv2.imread('input/ship.jpg')
gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_im)
cv2.waitKey(5000)

print(gray_im)
print('Type:', type(gray_im))
print('Shape:', gray_im.shape)
cv2.imwrite('output/gray_ship.jpg', gray_im)

print('Done.')

'''
Greyscale, pixel is no more a tuple, it is one-dimentional black-and-white data.

[[128 128 128 ... 129 128 132]
 [125 125 125 ... 129 128 130]
 [124 125 125 ... 129 129 130]
 ...
 [ 20  21  19 ...  38  39  37]
 [ 19  22  21 ...  41  42  37]
 [ 21  24  25 ...  36  37  32]]
Type: <class 'numpy.ndarray'>
Shape: (1118, 1577)

'''