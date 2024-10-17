from flask import Flask, render_template

app = Flask(__name__)


@app.after_request
def add_security_headers(response):
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response


@app.route("/")
def index():
    return render_template("home/index.html")


@app.route("/challenge")
def challenge():
    return render_template("challenge/challenge.html")


if __name__ == "__main__":
    app.run(debug=True)
