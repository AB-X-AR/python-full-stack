from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def homepage(name):
    return render_template("home.html")
    
@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

@app.route('/user/<name>')
def user(name):
    return render_template("home.html", username=name)

@app.route('/square/<int:num>')
def squared(num):
    snum = num ** 2
    return render_template("home.html", pizza=snum)

@app.route('/items')
def items():
    datai = ["Flask", "Jinja2", "Html"]
    return render_template("home.html", tech=datai)




if __name__ == "__main__":
    app.run(debug=True)