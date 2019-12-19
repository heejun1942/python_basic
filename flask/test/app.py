from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

@app.route('/hi')
def hi():
    name = "김희준"
    return render_template('hi.html', html_name = name)