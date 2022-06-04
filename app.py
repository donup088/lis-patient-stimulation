from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return render_template('tv.html')


@app.route('/first')
def first():  # put application's code here

    return render_template('first.html')


if __name__ == '__main__':
    app.run()
