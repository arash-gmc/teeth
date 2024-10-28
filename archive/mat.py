import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.optimize import curve_fit

# Load your image
img = mpimg.imread('imgs/figo.jpg')
# plt.imshow(img)
# plt.show()


# Define the curve function you want to fit (e.g., a linear function)
def model_func(x, a, b,c):
    return a * x**2 + b * x + c

# Generate some sample data points (replace with your actual data)
x_data = np.array([100, 200, 300, 400, 500])
y_data = np.array([200, 300, 500, 700, 1100])

# Fit the model to your data
params, covariance = curve_fit(model_func, x_data, y_data)

# Generate x values for plotting the fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = model_func(x_fit, *params)

# Create the plot
plt.imshow(img, extent=[0, 600, 0, 1000])  # Adjust extent to match your image and axis limits
plt.scatter(x_data, y_data, color='red', label='Data Points')
plt.plot(x_fit, y_fit, color='blue', label='Fitted Curve')

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Image Background with Points and Fitted Curve')
plt.legend()

# Show the plot
plt.show()


























# from PIL import Image

# import matplotlib.pyplot as plt
# import numpy as np

# img = np.asarray(Image.open('./imgs/figo.jpg'))
# matplotlib
# plt.imshow(img)

# lum_img = img[:, :, 0]
# plt.imshow(lum_img)




























# import matplotlib.pyplot as plt
# import numpy as np

# fig,ax = plt.subplots()

# ax.plot([1,2,3,4,5,6,7],[2,5,7,1,3,5,0,])

# plt.show()