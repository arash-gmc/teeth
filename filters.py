import cv2
import numpy as np
from detect import detect

# Load image and convert to grayscale
# image = cv2.imread('imgs/figo.jpg')
image,_  = detect('imgs/figo.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply CLAHE for contrast normalization
clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
equalized = clahe.apply(gray_image)
#cv2.imshow('Eq', equalized)

# Correct illumination variations
blurred = cv2.GaussianBlur(equalized, (31, 31), 0)
corrected = cv2.subtract(equalized, blurred)
corrected = cv2.normalize(corrected, None, 0, 255, cv2.NORM_MINMAX)
# cv2.imshow('cc', corrected)

# Smooth the image
smoothed = cv2.GaussianBlur(corrected, (5, 5), 0)
# cv2.imshow('ss', smoothed)
# Apply Canny edge detection
edges = cv2.Canny(smoothed, 120, 140)
edges_nopre = cv2.Canny(gray_image, 120, 140)

# Display the result
cv2.imshow('Edges', edges)
cv2.imshow('No Pre', edges_nopre)
cv2.waitKey(0)
cv2.destroyAllWindows()
