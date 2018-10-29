from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/index1')
def demo_23():
    return render_template('demo_23.html')


@app.route('/answer')
def answer():
    return render_template('answer.html')


@app.route('/index2')
def demo_24():
    return render_template('demo_24.html')


@app.route('/index3')
def demo_25():
    return render_template('demo_25.html')


@app.route('/index4')
def demo_26():
    return render_template('demo_26.html')


@app.route('/index_week')
def demo_week():
    return render_template('demo_week.html')

@app.route('/')
def love():
    return render_template('love.html')

if __name__ == '__main__':
    app.run()
