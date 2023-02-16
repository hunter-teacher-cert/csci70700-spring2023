from flask import Flask
from flask import render_template

import random

app = Flask(__name__)



@app.route('/')
def index():
    return '<h1>Hello from Flask!<h1>'

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/lucky')
def lucky():
  number = random.randrange(100)
  return render_template("lucky.html",num = number)

@app.route("/temp_demo")
def temp_demo():
  data = {"l" : ["one","one and a half", "two","three"],
         "first": "Humphrey",
         "last": "Bogart"}
  print(data)
  return render_template("template_demo.html",name="Snoopy",d=data,r = random.randrange(100))

app.run(host='0.0.0.0', port=81)
