from flask import Flask, render_template, Response
import cv2
import pickle
import cvzone
import numpy as np

app = Flask(__name__)

cap = cv2.VideoCapture('static/parking_vid.mp4')
with open('Parking', 'rb') as f:
    posList = pickle.load(f)

width, height = 110, 45

def generate_frames():
    while True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, img = cap.read()
        if not success:
            break

        # Image processing
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

            if count < 900:
                color = (255, 255, 0)
                space += 1
            else:
                color = (0, 0, 255)
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 2)
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0)

        cvzone.putTextRect(img, f"Free: {space}", (100, 50), scale=3, thickness=5, offset=20)

        # Convert to JPEG
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        # Stream frame to browser
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('display.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
