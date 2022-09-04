import cv2

img = cv2.imread('../../data/lab8.png')

img1 = img[5:1300, 555:3015]
img2 = cv2.Canny(img1, 0, 200)

th, thresh = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)
snowflake = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
print(str(len(snowflake)))

cv2.imshow("Snowflake", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
