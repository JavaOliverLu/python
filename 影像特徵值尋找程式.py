##SIFT ORB FAST HARIS SHITOM
#此程式參考網路上其他範例並且修改參數進行測試，在此作紀錄
import cv2
import numpy as np

# Reading the image and converting the image to B/W
image = cv2.imread('blur_visual_cloud_mascut_16263_20220820_1038LT.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = np.float32(gray_image)

# Applying the function
dst = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)

# dilate to mark the corners
dst = cv2.dilate(dst, None)
image[dst > 0.01 * dst.max()] = [0, 255, 0]
cv2.imwrite('HARIS.jpg', image)


############

image = cv2.imread("blur_visual_cloud_mascut_16263_20220820_1038LT.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying the function
corners = cv2.goodFeaturesToTrack(
    gray_image, maxCorners=50, qualityLevel=0.02, minDistance=20)
corners = np.float32(corners)

for item in corners:
    x, y = item[0]
    x = int(x)
    y = int(y)
    cv2.circle(image, (x, y), 6, (0, 255, 0), -1)
cv2.imwrite('shitom.jpg', image)

############
image = cv2.imread('blur_visual_cloud_mascut_16263_20220820_1038LT.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying the function
sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray_image, None)


# Applying the function
kp_image = cv2.drawKeypoints(image, kp, None, color=(
    0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('SIFT.jpg', kp_image)
############
image = cv2.imread('blur_visual_cloud_mascut_16263_20220820_1038LT.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Applying the function
fast = cv2.FastFeatureDetector_create()
fast.setNonmaxSuppression(False)


# Drawing the keypoints
kp = fast.detect(gray_image, None)
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 255, 0))
cv2.imwrite('FAST.jpg', kp_image)



###########
image = cv2.imread('blur_visual_cloud_mascut_16263_20220820_1038LT.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying the function
orb = cv2.ORB_create(nfeatures=2000)
kp, des = orb.detectAndCompute(gray_image, None)

# Drawing the keypoints
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 255, 0), flags=0)
cv2.imwrite('ORB.jpg', kp_image)
