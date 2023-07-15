import os
from flask import Flask, render_template, request
from google.cloud import logging

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
    client = logging.Client(project=project_id)
    logs = client.list_entries(filter_='logName:"cloudaudit.googleapis.com%2Factivity"')
   
    return render_template('logs.html', logs=list(logs))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))