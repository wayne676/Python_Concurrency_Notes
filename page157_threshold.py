# ch8/example3.py

import cv2

im = cv2.imread('input/ship.jpg')
gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, custom_thresh_im = cv2.threshold(gray_im, 127, 255, cv2.THRESH_BINARY)
# cv2.imwrite('output/custom_thresh_ship.jpg', custom_thresh_im)

print('Done.')

'''

categorizing each pixel into different groups, also known as image segmentation

@param src, input array (multiple-channel, 8-bit or 32-bit floating point).
@param thresh, threshold value.
@param maxval, maximum value to use with the (#THRESH_BINARY and #THRESH_BINARY_INV) thresholding
types.
@param type, thresholding type (see #ThresholdTypes).

threshold type:
    THRESH_BINARY: if pixel is greater than thresh, then it is set to maxval otherwise it is set to 0
    THRESH_BINARY_INV: on the contrary to THRESH_BINARY, pixel is 0 if it is greater than thresh, otherwise it is set to maxval
    THRESH_TOZERO: pixel does not change if its value greater than maxval, rest of the pixel value are set to 0
    THRESH_TOZERO_INV: on the contrary to THRESH_TOZERO
    THRESH_TRUNC: if pixel value is greater than thresh, then use thresh, other values remain same

'''