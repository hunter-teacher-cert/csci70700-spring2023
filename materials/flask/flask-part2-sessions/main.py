from flask import Flask,render_template
from flask import session

app = Flask(__name__)
app.secret_key="something"

@app.route('/')
def index():
  if "count" not in session:
    session["count"] = 0
  session['count'] = session['count'] + 1
  return render_template("index.html",session=session)        

app.run(host='0.0.0.0', port=81, debug=True)
