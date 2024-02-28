from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    processed_result = f"You entered: {user_input}"
    return processed_result

if __name__ == '__main__':
    app.run(debug=True)

# def display_results(evaluation_results):
#     print("\nConfusion Matrix:")
#     print(evaluation_results['confusion_matrix'])
#     print("\nAccuracy:", evaluation_results['accuracy'] * 100, "%")
