from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template('tv.html')


@app.route('/first')
def first():

    return render_template('first.html')


@app.route('/test')
def test():

    return render_template('test.html')


@app.route('/test2')
def test2():

    return render_template('test2.html')


@app.route('/test3')
def test3():

    return render_template('test3.html')


@app.route('/test4')
def test4():

    return render_template('test4.html')


if __name__ == '__main__':
    app.run()
