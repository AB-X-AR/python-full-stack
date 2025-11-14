from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

feeds = []



def get_db():
    conn = sqlite3.connect('userfeedback.db')
    conn.row_factory = sqlite3.Row #it lets us : row['name'] instead of row[1]
    return conn

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/adduser', methods=['POST'])
def adduser():
    uname = request.form['username']
    email = request.form['email']
    conn = get_db()
    conn.execute("INSERT INTO userfeeds (uname, email) VALUES (?, ?)", (uname, email))
    conn.commit()
    conn.close()
    return redirect("/allusers")

@app.route('/allusers') 
def allusers():
    conn = get_db()
    rows = conn.execute("SELECT * FROM userfeeds").fetchall()
    conn.close()
    return render_template("allusers.html", users=rows)


if __name__ == "__main__":
    app.run(debug=True)