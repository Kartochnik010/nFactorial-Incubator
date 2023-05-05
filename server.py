import json
from flask import Flask, render_template
from pkg import bgram

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/index')
def index():
    bigram_probs = bgram.train(bgram.get_names('names.txt'))
    data_json = json.dumps(bigram_probs)
    names = []

    for i in range(10):
        names.append(bgram.generate_name(bigram_probs))

    return render_template("index.html", data=data_json, names=names)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
