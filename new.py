
from detect import detect
from skimage import io, filters, exposure, feature, color
import matplotlib.pyplot as plt
import numpy as np

color_img,_,points,end_point = detect('imgs/pitt.jpg')

img = color.rgb2gray(color_img)

height,width = img.shape


equalized = exposure.equalize_adapthist(img, clip_limit=0.03)

smoothed = filters.gaussian(equalized, sigma=1.0)

edges = feature.canny(smoothed, sigma=1.2, low_threshold=0.3, high_threshold=0.5)

x,y,num = zip(*points)

coefficients = np.polyfit(x, y, 2)


x_fit = np.linspace(x[1], x[-2], x[-2]-x[1])
y_fit = coefficients[0] * x_fit**2 + coefficients[1] * x_fit + coefficients[2]



whiteness = []
for c in range (80):
    white=0    
    for i in range(len(x_fit)):
        if edges[int(y_fit[i]-c),int(x_fit[i])] :
            white += 0.6
        if edges[int(y_fit[i]-c-1),int(x_fit[i])] :
            white += 0.2
        if edges[int(y_fit[i]-c+1),int(x_fit[i])] :
            white += 0.2
    if y_fit[0]-c< end_point[1] :
        break
    whiteness.append(white/len(x_fit))

c_extermums = []

whitness_extermums = []
for i in range(3,len(whiteness)-1):
    if whiteness[i]>whiteness[i-1] and whiteness[i]>whiteness[i+1] :
        whitness_extermums.append(whiteness[i])
        c_extermums.append(i)

np_tot = np.array(whitness_extermums)
np_c = np.array(c_extermums)

top_extermums = np_c[np.argsort(np_tot)[::-1]][:3]


fig1 = plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img,cmap='gray')
plt.scatter(x,y,color='red',s=30)



for c in top_extermums:
    plt.plot(x_fit, y_fit-c, color='green', linewidth=1, label='Fitted 2nd-Degree Curve')


plt.title('Original Image')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.scatter(x,y,color='red',s=10)
plt.title('Canny Edge Detection')
plt.axis('off')

fig2 = plt.figure()
plt.plot(range(len(whiteness)),whiteness)

    

# Show the images
plt.tight_layout()
plt.show()










# clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
# img = clahe.apply(img)

# blurred = cv2.GaussianBlur(img, (31, 31), 0)
# corrected = cv2.subtract(img, blurred)
# img = cv2.normalize(corrected, None, 0, 255, cv2.NORM_MINMAX)

# img = cv2.GaussianBlur(img, (5, 5), 0)

# cany2 = cv2.Canny(img,100,150)




# cany = feature.canny(img,2,3,5)




# plt.imshow(cany, cmap='gray')
# plt.show()


