from flask import Flask
from flask import request
import studentrank as str
app = Flask(__name__)

@app.route('/')
def home():
    #stuname = str.main()
    return f"Hello there I am Mashik" # {stuname}

@app.route('/about')
def about():
    return "This is a About Page "

@app.route('/contact')
def contact():
    return "This is the Contact Page "

#strom = str.main()

@app.route('/user/<username>')
def greetuser(username):
    return f"Hello {username}! Welcome to Flask "

@app.route('/search')
def search():
    item = request.args.get('item')
    for i in str.stutable():
        if item == i:
            return f"Students Found with name : {item}"
        else:
            return f"Student {item} not found "

@app.route('/welcome')
def welcome():
    return """
        <h1> Welcome Abxar</h1>
        <h3>To Flask Project<h3>
        <p>Lorem Ipsum jsdnfjnsd fnsdifisdnifniweninien gioneg Detected change in 'e: PROJECTS PYTHON FLASKPYT Day1app.py', reloading </p>
        <a href='/about' > Go to About </a>
        <a href='/search?item=Mashik'>Search for students </a>
    """

@app.route('/square/<int:num>')
def squared(num):
    snum = num ** 2
    return f"The squarerd of {num} is {snum} "
    
@app.route('/sum/<int:a>/<int:b>')
def sumofab(a, b):
    return f"{a} + {b} = {a+b}"

@app.route('/reversed/<word>')
def revs(word):
    newrore = word[::-1]
    print(newrore)
    return f"Reversed : {newrore}"

@app.route('/info')
def infor():
    lang = request.args.get('lang')
    level = request.args.get('level')
    return f"""
        <h2>Lang: {lang}</h2>
        <h3>Level : {level}</h3>
    """


if __name__=="__main__":
    app.run(debug=True)




