from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/buy")
def buy():
    return render_template("buy.html")
