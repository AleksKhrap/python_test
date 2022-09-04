import cv2
# import numpy as np
img = cv2.imread("C:\\Users\\Alexandr\\Desktop\\Mustang.jpg")

y, x = img.shape[:2]
crop1 = img[:, :x//2].copy()
crop2 = img[:, x//2:]

img[:, :x//2] = crop2
img[:, x//2:] = crop1

# img = np.roll(img, img.shape[1]//2, axis=1)
cv2.imshow("Mustang", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
