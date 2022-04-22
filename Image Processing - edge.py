import cv2
import matplotlib.pyplot as plt


image = cv2.imread('x.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 35, 5)
plt.imshow(image)
plt.imshow(canny)





