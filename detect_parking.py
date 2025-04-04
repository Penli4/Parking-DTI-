from flask import Flask, render_template
import cv2
import pickle
import cvzone
import numpy as np

app = Flask(__name__)


def process_parking_image():
    width, height = 150, 200
    img = cv2.imread('static/parking_lot.jpg')
    print("Processing parking image...")
    with open('Parking', 'rb') as f:
        posList = pickle.load(f)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    space = 0
    for pos in posList:
        x, y = pos
        imgCrop = imgDilate[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)
        if count < 3500:
            color = (255, 255, 0)
            space += 1
        else:
            color = (0, 0, 255)
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 2)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0)
    cvzone.putTextRect(img, f"{space}", (100, 50), scale=3, thickness=5, offset=20)

    cv2.imwrite('static/result.jpg', img)


@app.route('/')
def home():
    process_parking_image()
    return render_template('display.html')


if __name__ == '__main__':
    app.run(debug=True)
