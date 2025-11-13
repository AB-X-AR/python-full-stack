from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

feeds = []

def get_db():
    conn = sqlite3.connect('feedbackstable.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return cursor, conn

def init_db():
    with get_db() as conn:
        cursor.execute('''CREATE TABLE IF NOT EXISTS feedbackstable (id INTEGER PRIMARY KEY AUTOINCREMENT, uname TEXT, perfeedback TEXT)''')

init_db()

@app.route('/')
def home():
    cursor.execute("SELECT * FROM feedbackstable.db")
    return render_template("home.html")


@app.route('/addfeedback', methods=['POST'])
def feedbacks():
    username = request.form['username']
    feedback = request.form['feedback']
    feeds.append(username)
    feeds.append(feedback)
    return render_template('addfeedback.html', username=username, feedback=feedback)

print(feeds)



if __name__ == "__main__":
    app.run(debug=True)