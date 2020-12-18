from cv2 import cv2
import numpy as np
import time
import keyboard

# empty function
def foo(x):
    pass

# init webcam 
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(3, 720)
