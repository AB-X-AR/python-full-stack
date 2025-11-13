from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

global_validcreds = {'adam':'adam', 'bison':'unsung', 'admin':'admin'}

@app.route('/')
def home():
    return render_template("index.html")

#LOGIN PAGE
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method ==  'POST':
        user = request.form['username']
        passi = request.form['password']
        if user in global_validcreds:
            posto = global_validcreds[user]
            print(f"Posto {posto} for User {user}")
            if posto == passi:
                return render_template("dashboard.html", username=user)
            else:
                return f" Wrong Password "
        else:
            return f"User Not Found"
    return render_template("login.html")


#REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        global_validcreds[user] = password
        print(global_validcreds)
        return redirect("/login")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)



