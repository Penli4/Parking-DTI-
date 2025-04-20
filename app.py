from flask import Flask, render_template, request, redirect, url_for, session, Response, jsonify
import cv2
import pickle
import cvzone
import numpy as np

app = Flask(__name__)
app.secret_key = 'secret-key'

users = {"Diya": "123456"}

# Parking detection variables
cap = cv2.VideoCapture('static/parking_vid.mp4')
with open('Parking', 'rb') as f:
    posList = pickle.load(f)

# Add row and column information for each parking spot
parking_info = {}
for i, pos in enumerate(posList):
    row = i // 5 + 1  # Assuming 5 spots per row, adjust as needed
    col = i % 5 + 1  # Column number
    parking_info[tuple(pos)] = {"row": row, "col": col}

width, height = 110, 45

# Global variable to store available spaces for the web interface
available_spaces = {"count": 0, "locations": []}

def generate_frames():
    global available_spaces

    while True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, img = cap.read()
        if not success:
            break

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        space = 0
        free_spaces = []

        for pos in posList:
            x, y = pos
            imgCrop = imgDilate[y:y + height, x:x + width]
            count = cv2.countNonZero(imgCrop)

            if count < 900:
                color = (255, 255, 0)
                space += 1
                pos_tuple = tuple(pos)
                if pos_tuple in parking_info:
                    free_spaces.append({"row": parking_info[pos_tuple]["row"], "col": parking_info[pos_tuple]["col"]})
                else:
                    free_spaces.append({"row": "-", "col": "-"})
            else:
                color = (0, 0, 255)

            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 2)
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0)

        # Update the message with row and column information
        if free_spaces:
            message = f"Free: {space}"
        else:
            message = f"Free: {space} | No spots available"

        cvzone.putTextRect(img, message, (50, 50), scale=2, thickness=3, offset=20)

        # Update global variable for web interface
        available_spaces = {
            "count": space,
            "locations": [{"row": spot["row"], "col": spot["col"]} for spot in free_spaces]
        }

        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def frontpage():
    return render_template('frontpage.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('signup.html', error="Username exists")
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('display.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/available_spaces')
def get_available_spaces():
    return jsonify(available_spaces)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
