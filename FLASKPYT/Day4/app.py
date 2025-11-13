from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


#scursor.execute("INSERT INTO tasks (title, status) VALUES (?, ?)", ("Day 4 Learning Flask", "Complete"))


def get_db():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    
    return conn

def init_db():
    with get_db() as conn: #with get_db() as conn auto commits & closes after use.
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, status NOT NULL DEFAULT  'Pending')''')


init_db()

@app.route('/add')
def add():
    pass




if __name__ == "__main__":
    app.run(debug=True)


















"""#----- DATABASE SECTION ------

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''
                     CREATE TABLE IF NOT EXISTS tasks ( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        status TEXT NOT NULL DEFAULT 'Pending'
                     )
        ''')
        
init_db()

# --- Routes ---

@app.route('/')
def index():
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY id DESC').fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/edit')
def edit 
"""