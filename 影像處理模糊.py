import cv2
import matplotlib.pyplot as plt
###以下程式皆參考網路資料並且更改參數，在此做個紀錄
#高斯模糊
image = cv2.imread('blur_visual_cloud_mascut_16263_20220820_1038LT.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 35, 5)
plt.imshow(image)
plt.imshow(canny)

##一般的模糊
imgblur = cv2.imread('visual_cloud_mascut_16263_20220820_1038LT.jpg')
filename_blur='blur_visual_cloud_mascut_16263_20220820_1038LT.jpg'
outputblur = cv2.blur(imgblur, (10, 10))
cv2.imwrite(filename_blur, outputblur)
