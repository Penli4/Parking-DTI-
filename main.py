import cv2
import pickle
import cvzone
import numpy as np

img = cv2.imread('dti.jpg')

with open('Parking', 'rb') as f:
    posList = pickle.load(f)

width, height = 150, 200

def check(imgPro, img):
    space = 0
    for pos in posList:
        x, y = pos
        imgcrop = imgPro[y:y+height, x:x+width]
        pixel_count = cv2.countNonZero(imgcrop)

        cvzone.putTextRect(img, str(pixel_count), (x, y + height - 3), scale=1, thickness=2, offset=0)

        if pixel_count < 3500:
            color = (255, 255, 0)
            space += 1
        else:
            color = (0, 0, 255)
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 2)
    cvzone.putTextRect(img, str(space), (100, 50), scale=3, thickness=5, offset=20)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
imgMedian = cv2.medianBlur(imgThreshold, 5)

kernel = np.ones((3, 3), np.uint8)
imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

check(imgDilate, img)

cv2.imshow("Parking Lot", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
