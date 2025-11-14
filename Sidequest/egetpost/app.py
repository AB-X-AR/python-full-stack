from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process_get', methods=['GET', 'POST'])
def process_get():
    if request.method == "GET":
        user = request.args.get("username")
        print("Request BTS : ", request.args)
        return f"User: {user}"
    elif request.method == "POST":
        user = request.form["username"]
        return f"User : {user} by post "
    else:
        return f"Not working !!!"

if __name__ == "__main__":
    app.run(debug=True)