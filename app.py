from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/dash")
def dashboard():
  return render_template("dash.html")

@app.route ("/")
def home():
  return "hi"

@app.route("/landing")
def land():
  return render_template("landing.html")


if __name__=="__main__":
  app.run(debug="True")