import json
import sqlite3

from flask import Flask, request,session 
from flask import render_template


app = Flask(__name__)
app.secret_key="something"


from flask_cors import CORS
CORS(app)

@app.route("/login",methods=['POST'])
def login():
    print(request.json['name'])
    name = request.json['name']
    print(request.json['password'])
    password = request.json['password']
    # we would really check this against a database
    # with usernames and passwords
    if (name=='z' and password=='12345'):
        result = {'token':1}
    else:
        result = {'token':0}
    return json.dumps(result)

@app.route("/get_movies",methods=['POST'])
def get_movies():
    token = request.json['token']
    # real world we'd also get the username
    # and check to make sure the username/token
    # are valid
    if token!=1:
        return json.dumps({'status':"Invalid Token",'data':[]})

    
    conn = sqlite3.connect('movies.db')
    q = 'select * from movies where genre="'+request.json['q']+'";'
    res = conn.execute(q)
    movies = [x for x in res]
    print(movies)
    return json.dumps({'status':"Success",'data':movies})


@app.route("/")
def index():
    return render_template("index.html")



app.run(host="0.0.0.0",port=5000,debug=True)
