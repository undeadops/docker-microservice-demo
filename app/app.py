## App micro service
# Will server templated HTML page from backend rest API on data service
import logging
import os
import requests

from flask import Flask, render_template, request, redirect, url_for

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

app = Flask(__name__)

API_HOST='http://localhost:5000'

def _feed_moby():
    # DATA URL Server
    URL=API_HOST+'/api/v1/feed/'
    r = requests.put(URL, data={ 'data': os.environ['HOSTNAME'] })
    return r

def _count_feed():
    URL=API_HOST+'/api/v1/'
    r = requests.get(URL)
    return r

@app.route('/feed')
def feed():
    results = _feed_moby()
    return redirect(url_for('index'), 302)

@app.route('/')
def index():
    message="Hello World, Joining you from Container ID: %s" % os.environ['HOSTNAME']

    num_feeds = _count_feed()
    feed_count = num_feeds.json()
    return render_template('layout.html', message=message, feed_count=feed_count['feedings'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
