from flask import Flask, render_template, request, url_for


app = Flask(__name__)

global_validcreds = {'adam':'adam', 'bison':'unsung', 'admin':'admin'}


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

if __name__ == "__main__":
    app.run(debug=True)



