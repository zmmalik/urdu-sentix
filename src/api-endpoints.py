from flask import Flask

app = Flask(__name__)

@app.route('/cb', methods=['GET'])
def cb():
    return 200


if __name__ == '__main__':
    app.run(debug=True)
