from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

"""@app.route('/')
def home():
    return render_template('index.html')"""

@app.route('/hello')
def hello():
    user = request.args.get('name', 'guest') #Guest is default if no name
    tech = ['Python', 'JavaScript', 'HTML', 'CSS', 'JAVA']
    return render_template('index.html',user=user, tech=tech)

@app.route('/sidequest')
def sidequest():
    user = request.args.get('user', 'guest') #Guest is default if no name
    place = request.args.get('place', 'India')
    print("DEBUG: user =", user)
    return render_template('sidequestmain.html', user=user, place=place)

@app.route('/squared/<int:num>')
def squared(num):
    snum = num ** 2
    return f"The square of {num} : {snum}"

@app.route('/api/data') #call using :5000/api/data
def api_data():
    data = {'name':'Abxar', 'role':'Cyber Security Researcher'}
    return jsonify(data)

@app.route('/go') #Redirect to main page with name = 'RedirectedUnknownUser'
def go():
    return redirect(url_for('hello', name='RedirectedUnknownUser'))



 

if __name__ == "__main__":
    app.run(debug=True)