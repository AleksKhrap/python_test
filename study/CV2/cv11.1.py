import numpy as np
import cv2

cap = cv2.VideoCapture(0)
movie = cv2.VideoCapture('data/movie1.mp4')
ret, frame = cap.read()
img = cv2.imread('../../data/ducks.jpg')
MIN_MATCH_COUNT = 10

while True:
    ret, frame = cap.read()
    ret1, frame1 = movie.read()
    sift = cv2.SIFT_create()

    try:
        kp1, des1 = sift.detectAndCompute(img, None)
        kp2, des2 = sift.detectAndCompute(frame, None)

        bf = cv2.BFMatcher()

        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        good = []
        for i in range(50):
            good.append(matches[i])

        if len(good) > MIN_MATCH_COUNT:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            h, w = img.shape[:2]
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, M)
            frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)

            h1, w1 = img.shape[:2]
            frame1 = cv2.resize(frame1, (w1, h1))

            h2, w2 = frame.shape[:2]
            warped_img = cv2.warpPerspective(frame1, M, (w2, h2))

            mask2 = np.zeros(frame.shape, dtype=np.uint8)
            roi_corners = np.int32(dst)
            filled_mask = mask2.copy()
            cv2.fillConvexPoly(filled_mask, roi_corners, (255, 255, 255))
            inverted_mask = cv2.bitwise_not(filled_mask)
            masked_image = cv2.bitwise_and(frame, inverted_mask)

            output = cv2.bitwise_or(warped_img, masked_image)

            cv2.imshow("Ducks", output)
        else:
            cv2.imshow("Ducks", frame)

    except cv2.error:
        cv2.imshow("Ducks", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()
