from flask import Flask,render_template
app=Flask(__name__)
# import sqlite3


@app.route('/')
def home():
    return render_template('index.html')
app.run()