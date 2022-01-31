from flask import Flask
import random

app = Flask(__name__)

@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  s = "<h1>Your lucky number is: "
  s = s + str(i)
  s = s + "</h1>"
  return s

@app.route("/")
def index():
  return "<h1>Hello World from Repl.it!</h1>"


app.run(host="0.0.0.0",port=5000,debug=True)
