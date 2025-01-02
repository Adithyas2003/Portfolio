from flask import Flask,render_template
app=Flask(__name__)
# import sqlite3


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



app.run()