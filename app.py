from flask import Flask, render_template, request, redirect, url_for, session, send_file
from detect_parking import process_parking_image

app = Flask(__name__)
app.secret_key = 'secret-key'

users = {"Diya": "123456"}
parking_data_path = 'Parking'

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
    process_parking_image()
    return render_template('display.html')
if __name__ == '__main__':
    app.run(debug=True)
