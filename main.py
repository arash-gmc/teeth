from detect import detect
import numpy as np
import cv2
from skimage import io, feature, color

result = detect('imgs/arash41.jpg')

image = result[0]





edges = cv2.Canny(image, 150, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100)



cv2.imshow('edge',image)


cv2.waitKey(0)

