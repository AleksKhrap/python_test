import numpy as np
import cv2
import os
import requests
from bs4 import BeautifulSoup


def parse(club_name):
    url = 'https://premierliga.ru/clubs/'
    if club_name == 'pfc-cska':
        url += 'pfc-cska'
    if club_name == 'lokomotiv':
        url += 'lokomotiv'
    if club_name == 'spartak':
        url += 'spartak'
    if club_name == 'zenit':
        url += 'zenit'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.select('.count p')
    a1 = a[1].text
    a2 = a[2].text
    a3 = a[3].text
    a4 = a[4].text
    s = [a1, a2, a3, a4]
    return s


cap = cv2.VideoCapture(0)
MIN_MATCH_COUNT = 15
images = sorted(os.listdir('../../data'))

while True:
    ret, frame = cap.read()
    orb = cv2.ORB_create()

    try:
        for filename in images:
            img = cv2.imread(os.path.join('../../data', filename))
            kp1, des1 = orb.detectAndCompute(img, None)
            kp2, des2 = orb.detectAndCompute(frame, None)

            FLANN_INDEX_LSH = 6
            index_params = dict(algorithm=FLANN_INDEX_LSH,
                                table_number=6,
                                key_size=12,
                                multi_probe_level=2)
            search_params = dict(checks=50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des1, des2, k=2)

            good = []

            try:
                for m, n in matches:
                    if m.distance < 0.7 * n.distance:
                        good.append(m)
            except:
                cv2.imshow("RPL", frame)

            if len(good) > MIN_MATCH_COUNT:
                src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                h, w = img.shape[:2]
                pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)
                if filename == images[0]:
                    frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 0, 255), 3, cv2.LINE_AA)
                    y, x = frame.shape[:2]
                    c = parse('pfc-cska')
                    y0, dy, text = 20, 20, 'CSKA' + '\nGames: ' + str(c[0]) + '\nWins:' + str(c[1]) + '\nDraws: ' \
                                   + str(c[2]) + '\nDefeats: ' + str(c[3])
                    for i, line in enumerate(text.split('\n')):
                        y1 = y0 + i * dy
                        cv2.putText(frame, line, (20, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.imshow("RPL", frame)
                if filename == images[1]:
                    frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)
                    y, x = frame.shape[:2]
                    c = parse('lokomotiv')
                    y0, dy, text = 20, 20, 'Lokomotiv' + '\nGames: ' + str(c[0]) + '\nWins:' + str(c[1]) + '\nDraws: ' \
                                   + str(c[2]) + '\nDefeats: ' + str(c[3])
                    for i, line in enumerate(text.split('\n')):
                        y1 = y0 + i * dy
                        cv2.putText(frame, line, (x - 150, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    cv2.imshow("RPL", frame)
                if filename == images[2]:
                    frame = cv2.polylines(frame, [np.int32(dst)], True, (255, 255, 255), 3, cv2.LINE_AA)
                    y, x = frame.shape[:2]
                    c = parse('spartak')
                    y0, dy, text = 20, 20, 'Spartak' + '\nGames: ' + str(c[0]) + '\nWins:' + str(c[1]) + '\nDraws: ' \
                                   + str(c[2]) + '\nDefeats: ' + str(c[3])
                    for i, line in enumerate(text.split('\n')):
                        y1 = y0 - i * dy
                        cv2.putText(frame, line, (x - 150, y - y1 - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                    (255, 255, 255), 2)
                    cv2.imshow("RPL", frame)
                if filename == images[3]:
                    frame = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3, cv2.LINE_AA)
                    y, x = frame.shape[:2]
                    c = parse('zenit')
                    y0, dy, text = 20, 20, 'Zenit' + '\nGames: ' + str(c[0]) + '\nWins:' + str(c[1]) + '\nDraws: ' \
                                   + str(c[2]) + '\nDefeats: ' + str(c[3])
                    for i, line in enumerate(text.split('\n')):
                        y1 = y0 - i * dy
                        cv2.putText(frame, line, (20, y - y1 - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                    cv2.imshow("RPL", frame)
            else:
                cv2.imshow("RPL", frame)

    except cv2.error:
        cv2.imshow("RPL", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()
