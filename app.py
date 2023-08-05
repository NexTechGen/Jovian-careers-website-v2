# flask is model & Flask,render_templete is class
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_jovin():
  return render_template(
    "home_bootstrap.html")  # home.html or home_bootstrap.html


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
