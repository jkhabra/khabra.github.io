from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/work')
def work():
    return render_template('work.html')
