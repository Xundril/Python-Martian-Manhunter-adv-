# flask_web/app.py
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/calc/<int:x>/<int:y>/<string:func>')
def calc(x, y, func):
    if func == 'sum':
        return render_template('calc.html', x=x, y=y, func="+", result=x + y)
    elif func == 'dif':
        return render_template('calc.html', x=x, y=y, func="-", result=x - y)
    elif func == 'mul':
        return render_template('calc.html', x=x, y=y, func="*", result=x * y)
    elif func == 'div':
        if y == 0:
            return render_template('calc.html', y=y)
        else:
            return render_template('calc.html', x=x, y=y, func="/", result=x / y)
    else:
        return render_template('calc.html', func="Null")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')