import os
import requests
from flask import Flask, request, redirect, url_for, send_from_directory, render_template

# Web Server Config
app = Flask(__name__)
app.config["DEBUG"] = False
app.config['UPLOAD_PATH'] = 'uploads'

# Method to display web page with upload form and button
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    message = request.args.get("message")
    return render_template('index.html', files=files, message=message)

@app.route('/', methods=['POST'])
def upload_files():
    # Extract file from HTTP upload by user
    uploaded_file = request.files['file']

    # Construct HTTP request with file to send to API server for classification
    files = {'file': uploaded_file.read()}
    config = open("config.txt", 'r')
    api_url = config.read() # URL is configurable in config.txt
    response = requests.post(api_url, files=files)
    
    # Redirect response from API server to update the classification category
    # and probability on original web page
    return redirect(url_for('index', message=response.text))

# Show image on web page 
@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

# Listen for requests on all network interfaces
app.run(host='0.0.0.0', port=5000)