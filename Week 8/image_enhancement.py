#image enhancement

import cv2
#read the image

img=cv2.imread('D:\\coding\\python\\Joy of computing using python\\Week 8\\photo2.png')

#preparation for CLAHE

clahe=cv2.createCLAHE()

#convert to gray scale image

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#AAPPLY ENHANCEMENT

enh_img = clahe.apply(gray_img)

#save it to a file

cv2.imwrite('D:\\coding\\python\\Joy of computing using python\\Week 8\\newphoto2.png', enh_img)
print('Done enhancing')