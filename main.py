from cv2 import cv2
import numpy as np
import time
import keyboard

# loading from previous setup
prev_values = True
# if prev_values:
    # penval = np.load('penval.py')

# video_stream = cv2.VideoCapture(0)

pen_img = cv2.resize(cv2.imread('icons/pen.jpg', 1), (50,50))
eraser_img = cv2.resize(cv2.imread('icons/eraser.jpg', 1), (50,50))
nopen_img = cv2.resize(cv2.imread('icons/nopen.jpg', 1), (50,50))

#####################
# test for icons
cv2.imshow("penimg", pen_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
