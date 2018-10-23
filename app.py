from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/')
def demo_23():
    return render_template('demo_23.html')


@app.route('/answer')
def answer():
    return render_template('answer.html')


if __name__ == '__main__':
    app.run()
