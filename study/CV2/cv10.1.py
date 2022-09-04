import numpy as np
import cv2

method = int(input('SIFT - 1'
                   '\nORB - 2\n'))
match = int(input('match - 1'
                  '\nknnMatch - 2\n'))
if method == 1 and match == 1:
    norm = int(input('L1 - 1'
                     '\nL2 - 2\n'))
if method == 2 and match == 1:
    norm = int(input('L1 - 1'
                     '\nL2 - 2'
                     '\nHAMMING - 3'
                     '\nHAMMING2 - 4'
                     '\nTYPE_MASK - 5\n'))

img = cv2.imread('../../data/ducks.jpg')

cap = cv2.VideoCapture(0)
MIN_MATCH_COUNT = 10
sift = cv2.SIFT_create()
orb = cv2.ORB_create()

while True:
    ret, frame = cap.read()

    try:
        if method == 1:
            kp1, des1 = sift.detectAndCompute(img, None)
            kp2, des2 = sift.detectAndCompute(frame, None)

            if match == 1:
                if norm == 1:
                    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
                if norm == 2:
                    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
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
                    cv2.imshow("EON", frame)
                else:
                    cv2.imshow("EON", frame)

            if match == 2:
                bf = cv2.BFMatcher()
                matches = bf.knnMatch(des1, des2, k=2)

                good = []
                for m, n in matches:
                    if m.distance < 0.7 * n.distance:
                        good.append(m)
                if len(good) > MIN_MATCH_COUNT:
                    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                    h, w = img.shape[:2]
                    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                    dst = cv2.perspectiveTransform(pts, M)
                    frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)
                    cv2.imshow("EON", frame)
                else:
                    cv2.imshow("EON", frame)

        if method == 2:
            kp1, des1 = orb.detectAndCompute(img, None)
            kp2, des2 = orb.detectAndCompute(frame, None)

            if match == 1:

                if norm == 1:
                    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
                if norm == 2:
                    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
                if norm == 3:
                    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                if norm == 4:
                    bf = cv2.BFMatcher(cv2.NORM_HAMMING2, crossCheck=True)
                if norm == 5:
                    bf = cv2.BFMatcher(cv2.NORM_TYPE_MASK, crossCheck=True)

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
                    cv2.imshow("EON", frame)
                else:
                    cv2.imshow("EON", frame)

            if match == 2:
                FLANN_INDEX_LSH = 6
                index_params = dict(algorithm=FLANN_INDEX_LSH,
                                    table_number=6,
                                    key_size=12,
                                    multi_probe_level=2)
                search_params = dict(checks=50)
                flann = cv2.FlannBasedMatcher(index_params, search_params)
                matches = flann.knnMatch(des1, des2, k=2)

                good = []

                for m, n in matches:
                    if m.distance < 0.7 * n.distance:
                        good.append(m)

                if len(good) > MIN_MATCH_COUNT:
                    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                    h, w = img.shape[:2]
                    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                    dst = cv2.perspectiveTransform(pts, M)
                    frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)
                    cv2.imshow("EON", frame)
                else:
                    cv2.imshow("EON", frame)

    except cv2.error:
        cv2.imshow("EON", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()
