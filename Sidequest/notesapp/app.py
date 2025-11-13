from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

tasks = ["Make Beef Burget", "Make Omlete"]

@app.route('/', methods=['GET', 'POST'])
def home():
    currenttask = tasks
    print(tasks)
    if request.method == 'POST':
        task = request.form.get('task')
        action = request.form.get('action')
        tasknumber = request.form.get('tasknumber')
        try:
            index = int(tasknumber)  # Convert to integer
        except (TypeError, ValueError):
            index = None
        
        if task:
            if action == 'add':
                tasks.append(task)
            elif action == 'update' and task and index is not None and 0 <= index < len(tasks):
                tasks[index] = task
            elif action == 'delete':
                tasks.remove(task)
    return render_template('home.html', tasks=currenttask)



if __name__=="__main__":
    app.run(debug=True)