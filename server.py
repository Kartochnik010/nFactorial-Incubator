from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/index')
def index():
    name = 'World'
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
