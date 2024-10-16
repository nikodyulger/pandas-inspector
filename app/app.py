from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home/index.html")


@app.route("/challenge")
def challenge():
    return render_template("challenge/challenge.html")
