import os
import requests
import time
from flask import Flask, request, redirect, url_for, send_from_directory, render_template

# Web Server Config
app = Flask(__name__)
app.config["DEBUG"] = False
app.config['UPLOAD_PATH'] = 'uploads'

# Display web page with upload form and button
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    message = request.args.get("message")
    time = request.args.get("time")
    return render_template('index.html', files=files, message=message, time=time)

# Upload image to web server to call API server for classification 
@app.route('/', methods=['POST'])
def upload_files():
    # Extract file from HTTP upload by user
    uploaded_file = request.files['file']

    # Construct HTTP request with file to send to API server for classification
    files = {'file': uploaded_file.read()}
    config = open("config.txt", 'r')
    api_url = config.read() # URL is configurable in config.txt
    start_time = time.time()
    response = requests.post(api_url, files=files)
    time_lapsed = time.time() - start_time

    # Redirect response from API server to update the classification category
    # and probability on original web page
    message = response.text
    return redirect(url_for('index', message=message, time=str(time_lapsed)))

# Show image on web page 
@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

# Listen for requests on all network interfaces
app.run(host='0.0.0.0', port=5000)