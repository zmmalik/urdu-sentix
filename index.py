from flask import Flask, render_template

from src.collect_real_time_comments.facebook import get_fb_comments
from src.collect_real_time_comments.instagram import get_insta_comments
from mock_data.mock_data_set import data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cb', methods=['GET'])
def cb():
    return 200

@app.route('/get-comments/<string:social>', methods=['GET'])
def get_comments(social):
    if social == 'facebook':
        return {"status": "OK", "status_code": 200, "data": {"comments": data}}
    elif social == 'instagram':
        return {"status": "OK", "status_code": 200, "data": {"comments": get_insta_comments()}}
    else:
        {"error": "some error"}
if __name__ == '__main__':
    app.run(debug=True)
