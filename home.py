from flask import Flask, render_template, request, redirect,send_from_directory
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/view_resume")
def view_resume():
    return send_from_directory(directory="static", path="ADITHYA S (Resume).pdf")

@app.route('/submit', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
      
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", 
                  (name, email, message))
        conn.commit()
        conn.close()

        return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)

