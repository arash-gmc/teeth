# for p in result[1]:
#     cv2.circle(result[0],(p[0],p[1]),3,(255,0,0),-1)

# canny = cv2.Canny(result[0],200,300)

# for i in range(5):
#     min= 100+50*i
#     max=100+50*i
#     cv2.imshow(str(max),cv2.Canny(result[0],min,max))


# sobel_x = cv2.Sobel(result[0], cv2.CV_64F, 1, 0, ksize=5)  # Horizontal edges
# sobel_y = cv2.Sobel(result[0], cv2.CV_64F, 0, 1, ksize=5)  # Vertical edges
# sobel_combined = cv2.magnitude(sobel_x, sobel_y)  # Combine both directions
# cv2.imshow('ff',sobel_y)

# blurred = cv2.GaussianBlur(image, (3, 3), 0)  # Apply Gaussian Blur
# laplacian = cv2.Laplacian(blurred, cv2.CV_64F)  # Apply Laplacian

# kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])  # Horizontal
# kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])  # Vertical

# prewitt_x = cv2.filter2D(image, -1, kernel_x)
# prewitt_y = cv2.filter2D(image, -1, kernel_y)
# prewitt_combined = cv2.magnitude(prewitt_x, prewitt_y)

# scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0)  # Horizontal edges
# scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)  # Vertical edges
# scharr_combined = cv2.magnitude(scharr_x, scharr_y)

# kernel_x = np.array([[1, 0], [0, -1]])
# kernel_y = np.array([[0, 1], [-1, 0]])

# roberts_x = cv2.filter2D(image, -1, kernel_x)
# roberts_y = cv2.filter2D(image, -1, kernel_y)
# roberts_combined = cv2.magnitude(roberts_x, roberts_y)

# _, binary_edges = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
