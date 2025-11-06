from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("feedback.html")

feedbacklist = []

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    feedback = request.form['feedback']
    with open('E:/PROJECTS/PYTHON/pyfullstack/FLASKPYT/Day2/templates/trash', 'a') as trashadd:
        trashadd.write(f"Name : {name}\nFeedback: {feedback}\nTime: {datetime.now()} \n{'-'*40}\n")
    feedbacklist.append({'name': name, 'fb': feedback})
    return render_template("thankyou.html", name=name, feedback=feedback)

@app.route('/allfeedbacks')
def collectfeedbacks():
    return render_template("allfeedbacks.html", all=feedbacklist)
    


if __name__=="__main__":
    app.run(debug=True)