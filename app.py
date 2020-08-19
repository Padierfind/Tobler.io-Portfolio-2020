print("In File: app.py")

from flask import Flask, Blueprint, render_template
app = Flask(__name__)


@app.route('/')
def display_index():
    return render_template('index_v1.html')


@app.route('/imprint')
def display_imprint():
    return render_template('imprint_v1.html')

@app.route('/buildorder')
def display_buildorder():
    return render_template('buildorder.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
