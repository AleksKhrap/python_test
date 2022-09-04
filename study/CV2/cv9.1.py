import cv2

img = cv2.imread('../../data/movie1.png')
img = cv2.resize(img, (900, 400))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture('data/movie1.mp4')
# sift = cv2.SIFT_create()
orb = cv2.ORB_create()
frame_count = 0
max = 0
fr = 0
time = 0

while True:
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count += 1
    mt = 0

    kp1, des1 = orb.detectAndCompute(img, None)
    kp2, des2 = orb.detectAndCompute(frame, None)

    if des2 is None:
        des2 = []

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    mt = int(len(matches))
    frame = cv2.drawMatches(img, kp1, frame, kp2, matches, None, flags=2)

    ''' SIFT
    kp1, des1 = sift.detectAndCompute(img, None)
    kp2, des2 = sift.detectAndCompute(frame, None)
    '''

    ''' 1 способ:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
            mt += 1
    frame = cv2.drawMatchesKnn(img, kp1, frame, kp2, good, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    '''

    ''' 2 способ:
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    mt = int(len(matches))
    frame = cv2.drawMatches(img, kp1, frame, kp2, matches, None, flags=2)
    '''

    if mt > max:
        max = mt
        fr = frame_count
        time = int(cap.get(cv2.CAP_PROP_POS_FRAMES)) / fps

    print('Frame: ', frame_count, 'Matches: ', mt, 'Max Matches: ', max, 'The desired frame: ', fr, 'Time: ', time)

    cv2.imshow("Strange", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

print('Max Matches: ', max, '\nThe desired frame: ', fr, '\nTime: ', time)

cap.release()
cv2.destroyAllWindows()
