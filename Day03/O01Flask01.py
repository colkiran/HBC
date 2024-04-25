
from flask import Flask

# __name__ will give the name of the current module - __main__
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello Sachin </h1>"

@app.route("/<usrname>")
def user(usrname):
    return f"<h2> {usrname} Welcome to web development using Flask  </h2>"


if __name__ == '__main__':
    app.run(debug = True,  port=5001)           # debug mode is not enabled