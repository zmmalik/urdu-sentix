from flask import Flask, render_template

from src.collect_real_time_comments.facebook import get_fb_comments
from src.collect_real_time_comments.instagram import get_insta_comments
from mock_data.mock_data_set_actual import data
from main import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cb', methods=['GET'])
def cb():
    return 200

@app.route('/get-comments/<string:social>', methods=['GET'])
def get_comments(social):
    comments = []
    if social == 'facebook':
        comments = data
    elif social == 'instagram':
        comments = data

    sentiments = main(comments)
    return {"status": "OK", "status_code": 200, "comments": sentiments}

if __name__ == '__main__':
    app.run(debug=True)
