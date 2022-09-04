import cv2
import numpy as np
import random

size = int(input('Введите размер: '))
N = int(input('Введите количество: '))
im = np.full((size, size, 3), 255, dtype=np.uint8)

r = size

for i in range(N):
    cv2.circle(im, (int(size / 2), int(size / 2)), int(r / 2), (random.randint(0, 255), random.randint(0, 255),
                                                                random.randint(0, 255)), 1)
    cv2.rectangle(im, (int(int(size / 2) - int((r / 2) / 2 ** 0.5)), int(int(size / 2) + int((r / 2) / 2 ** 0.5))),
                  (int(int(size / 2) + int((r / 2) / 2 ** 0.5)), int(int(size / 2) - int((r / 2) / 2 ** 0.5))),
                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 1)

    r = int(r / 2 ** 0.5)

cv2.imshow("Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
