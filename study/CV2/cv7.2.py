import cv2
import random
import numpy as np

y = int(input('Введите y: '))
x = int(input('Введите x: '))

im = []
for i in range(25):
    im.append(cv2.imread("C:\\Users\\Alexandr\\Desktop\\7_2\\"+str(i)+".jpg"))

for i in range(25):
    y1, x1 = im[i].shape[:2]
    y1 -= y
    x1 -= x
    y1 = random.randint(0, y1)
    x1 = random.randint(0, x1)
    im[i] = im[i][y1:y1 + y, x1:x1 + x]

random.shuffle(im)
col1 = np.vstack([im[0], im[1], im[2], im[3], im[4]])
col2 = np.vstack([im[5], im[6], im[7], im[8], im[9]])
col3 = np.vstack([im[10], im[11], im[12], im[13], im[14]])
col4 = np.vstack([im[15], im[16], im[17], im[18], im[19]])
col5 = np.vstack([im[20], im[21], im[22], im[23], im[24]])
res = np.hstack([col1, col2, col3, col4, col5])

cv2.imshow("Collage", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
