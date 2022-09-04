import cv2
import numpy as np


def vid():
    global r, d, t, s, f
    r = 0
    d = 0
    t = 0
    s = 0
    f = 0
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

        if cv2.waitKey(1) & 0xFF == ord('e'):
            r += 90
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('w'):
            r -= 90
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('z'):
            d += 1
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('c'):
            d -= 1
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('t'):
            t += 1
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('C:\\Users\\Alexandr\\PycharmProjects\\pythonProject\\data\\'+str(s)+'.jpg', frame)
            s += 1

        if cv2.waitKey(1) & 0xFF == ord('f'):
            f += 1
            vid3()
            break


def vid2():
    global r, d, t, s, f
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        if r > 0:
            if r % 360 == 90:
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            if r % 360 == 180:
                frame = cv2.rotate(frame, cv2.ROTATE_180)
            if r % 360 == 270:
                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            if r % 360 == 0:
                frame = frame

        if r < 0:
            if r % -360 == -90:
                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            if r % -360 == -180:
                frame = cv2.rotate(frame, cv2.ROTATE_180)
            if r % -360 == -270:
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            if r % -360 == 0:
                frame = frame

        if r == 0:
            frame = frame

        if d > 0:
            width = int(frame.shape[1] * 50 / (100 * abs(d)))
            height = int(frame.shape[0] * 50 / (100 * abs(d)))
            dim = (width, height)
            frame = cv2.resize(frame, dim)

        if d == 0:
            frame = frame

        if d < 0:
            width = int(frame.shape[1] * 100 * abs(d) / 50)
            height = int(frame.shape[0] * 100 * abs(d) / 50)
            dim = (width, height)
            frame = cv2.resize(frame, dim)

        if t % 2 == 1:
            cv2.circle(frame, (12, 12), 11, (255, 0, 255), 1)
            cv2.circle(frame, (12, 12), 9, (0, 255, 0), 1)
            cv2.circle(frame, (12, 12), 7, (255, 255, 0), 1)
            cv2.line(frame, (1, 23), (23, 1), (0, 69, 255), 1)
            cv2.line(frame, (1, 1), (23, 23), (0, 69, 255), 1)
            cv2.rectangle(frame, (1, 1), (23, 23), (0, 0, 255), 1)
            cv2.putText(frame, "Khrapov", (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        cv2.imshow('Camera stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

        if cv2.waitKey(1) & 0xFF == ord('e'):
            r += 90
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('w'):
            r -= 90
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('z'):
            d += 1
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('c'):
            d -= 1
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('t'):
            t += 1
            vid2()
            break

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('C:\\Users\\Alexandr\\PycharmProjects\\pythonProject\\data\\'+str(s)+'.jpg', frame)
            s += 1

        if cv2.waitKey(1) & 0xFF == ord('f'):
            f += 1
            vid3()
            break


def vid3():
    global f
    cap = cv2.VideoCapture(0)
    while True:
        frame = [0, 0, 0, 0, 0, 0]
        for i in range(6):
            ret, frame[i] = cap.read()

        if f % 2 == 1:
            frame[0] = frame[0]
            frame[1] = cv2.cvtColor(frame[1], cv2.COLOR_BGR2GRAY)
            frame[1] = cv2.Canny(frame[1], 100, 200)
            frame[1] = cv2.cvtColor(frame[1], cv2.COLOR_GRAY2BGR)
            frame[2] = cv2.GaussianBlur(frame[2], (9, 9), 10)
            kernel = np.array([[0.0, -1.0, 0.0],
                               [-1.0, 4.0, -1.0],
                               [0.0, -1.0, 0.0]])
            kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)
            frame[3] = cv2.filter2D(frame[3], -1, kernel)
            frame[4] = cv2.flip(frame[4], 1)
            frame[5] = cv2.blur(frame[5], (100, 100))

        if f % 2 == 0:
            vid()
            break

        for i in range(6):
            line1 = np.hstack([frame[0], frame[1], frame[2]])
            line2 = np.hstack([frame[3], frame[4], frame[5]])
            res = np.vstack([line1, line2])

        cv2.imshow('Camera stream', res)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

        if cv2.waitKey(1) & 0xFF == ord('f'):
            f += 1
            vid3()
            break


vid()
