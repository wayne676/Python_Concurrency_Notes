# ch8/example4.py

import cv2

im = cv2.imread('input/ship.jpg')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

mean_thresh_im = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imwrite('output/mean_thresh_ship.jpg', mean_thresh_im)

gauss_thresh_im = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imwrite('output/gauss_thresh_ship.jpg', gauss_thresh_im)

print('Done.')

'''
adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None)
    @param src Source 8-bit single-channel image.
    @param dst Destination image of the same size and the same type as src.
    @param maxValue Non-zero value assigned to the pixels for which the condition is satisfied
    @param adaptiveMethod Adaptive thresholding algorithm to use, see #AdaptiveThresholdTypes.
        The #BORDER_REPLICATE | #BORDER_ISOLATED is used to process boundaries.
    @param thresholdType Thresholding type that must be either #THRESH_BINARY or #THRESH_BINARY_INV,
    see #ThresholdTypes.
    @param blockSize Size of a pixel neighborhood that is used to calculate a threshold value for the
        pixel: 3, 5, 7, and so on.
    @param C Constant subtracted from the mean or weighted mean (see the details below). Normally, it
        is positive but may be zero or negative as well.
'''