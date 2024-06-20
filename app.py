from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='./static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fruits')
def fruit():
    return render_template('fruit.html')

if __name__ == '__main__':
    app.run(debug=True)