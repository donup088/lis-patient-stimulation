from flask import Flask, request
from flask import render_template

from analysis import analysis
from ssvep import ssvep

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


@app.route('/ssvep')
def assvep():
    idx = request.args.get('idx')
    date = request.args.get('date')
    print('assvep')
    print(idx, date)
    result = ssvep(idx, date)
    # result = [1, '2022-06-10_오후 8_55']
    print('ssvep 결과')
    print(result)
    return {"result": {
        'idx': int(result[0]),
        'date': result[1]
    }}


@app.route('/analysis')
def test5():
    print('데이터 분석!')
    result = analysis()
    # result = [1, '2022-06-10_오후 8_55']
    print(result)
    return {"result": {
        'idx': int(result[0]),
        'date': result[1]
    }}


@app.route('/rest')
def rest():
    idx = request.args.get('idx')
    date = request.args.get('date')

    return render_template('rest.html')


if __name__ == '__main__':
    app.run()
