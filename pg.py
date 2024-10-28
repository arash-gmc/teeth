from skimage import io, feature, color
from detect import detect
import cv2

# Load the image and convert it to grayscale
image = detect('imgs/figo.jpg')[0]
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = color.rgb2gray(image)



# Apply Canny edge detection
edges = feature.canny(gray_image, sigma=0.5, low_threshold=0.2, high_threshold=1)

# Display the result
import matplotlib.pyplot as plt
#plt.imshow(gray, cmap='gray')
plt.imshow(gray_image, cmap='gray')
plt.show()
