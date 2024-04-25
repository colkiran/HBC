
from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)
flag = False
app.secret_key = "hello"

@app.route("/")
def home():
    return render_template("index01.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        global flag
        flag = True
        return redirect(url_for("user", usr=user))
    else:
        flag = False
        if flag == False:
            flash("You have used get method......")
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    global flag
    if flag:
        flash("You have used the post method......")
    return render_template("result.html", usr=usr)

if __name__ == '__main__':
    app.run(debug=True)

