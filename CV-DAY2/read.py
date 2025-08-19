import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image2.jpg")
rows,cols=img.shape[:2]
(h, w) = img.shape[:2]

print(img.shape)

rect = cv2.rectangle(img,(300,300),(100,750),(50,50,50),2)
circle = cv2.circle(img,(30,30),50,(0,0,255),1)

RM = cv2.getRotationMatrix2D((w//2,h//2),45,1.0)
rotated = cv2.warpAffine(img, RM, (w,h))

plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()