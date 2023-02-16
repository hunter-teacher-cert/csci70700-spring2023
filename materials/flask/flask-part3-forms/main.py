from flask import Flask,session,render_template
from flask import request

app = Flask(__name__)
app.secret_key="askljaefd"

@app.route("/form-demo",methods=['GET','POST'])
def form_demo():
  
  if request.method == "GET":
    return render_template("form-demo.html")
  else:
    print(request.form)
    item = request.form['TODO']
    if "todo_list" not in session:
      session['todo_list'] = []

    if request.form['submit']=='doit':  
      l = session['todo_list']
      l.append(item)
      session['todo_list']  = l
    else:
      session['todo_list'] = []
      
    return render_template("form-demo.html",todos=session['todo_list'])
    
@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81,debug=True)
