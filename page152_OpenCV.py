# ch8/example1.py

import cv2

im = cv2.imread('input/ship.jpg')
cv2.imshow('Test', im)
cv2.waitKey(0) # press any key to move forward here

print(im)
print('Type:', type(im))
print('Shape:', im.shape)
print('Top-left pixel:', im[0, 0])

print('Done.')

'''
cv2.imread() takes in a path to an image file, cv2.imread读入的是BGR顺序
cv2.imshow() takes in a string and an images object, display it in a separate window and title of the window is the passed-in string
cv2.waitKey() should always follow the cv2.imshow(), it takes in a number and blocks the program for a corresponding number of 
    millisecodes unless the number is 0, in which case the user need presses a key to stop the block
[[[199 136  86]
  [199 136  86]
  [199 136  86]
  ...
  [198 140  81]
  [197 139  80]
  [201 143  84]]
...
 [[ 56  23   4]
  [ 59  26   6]
  [ 59  28   7]
  ...
  [ 79  43   7]
  [ 80  44   8]
  [ 75  39   3]]]
Above is the output (not complete output), type is Type: <class 'numpy.ndarray'>
Shape: (1118, 1577, 3) [cloumns, rows, dimention of pixel]
Top-left pixel: [199 136  86] [b, g, r]


'''