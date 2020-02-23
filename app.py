print("In File: app.py")

from flask import Flask, Blueprint, render_template
app = Flask(__name__)


@app.route('/')
def display_index():
    return render_template('index.html')


@app.route('/imprint')
def display_imprint():
    return render_template('imprint.html')


if __name__ == '__main__':
    app.run()