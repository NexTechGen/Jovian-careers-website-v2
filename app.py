from flask import Flask  # flask is model & Flask is class

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<h1>Hello, Ruzaith!</h1>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
