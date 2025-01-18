from flask import Flask,redirect,url_for,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MySQL_HOST'] = 'local host'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ' '
app.config['MySQL_DB'] = 'registered'
mysql=MySQL(__name__)
c = MySQL(app)

@app.route('/reg')
def page():
    return render_template('i.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/')
def reg():
    return render_template('reg.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/gdcal')
def gdc():
    return render_template('gdcal.html')

@app.route('/cal')
def cal():
    return render_template('cal.html')

@app.route('/users' , methods=['POST', 'GET'])
def users():
    if request.method =="POST":
        n =request.form["name"]
        e = request.form["email"]
        m = request.form["mobile"]
        p = request.form["password"]

        return render_template("data.html" , name =n ,email=e ,mobile=m, password=p)
    return render_template("data.html")

@app.route('/loginto' , methods=['POST', 'GET'])
def loginto():
    if request.method =="POST":
        n =request.form["name"]
        e = request.form["email"]
        p = request.form["password"]
        if e == "admin" and p == "admin":
            return render_template('dash.html', name = n)
        else:
            return render_template("reg.html")
    return render_template("dash.html")

@app.route('/cal' , methods=['POST','GET'])
def cale():
    if request.method == "POST":
        n = request.form['name']
        c = request.form['code']
        p = request.form['password']
        if p == 'admin':
            return render_template('cal.html', name = n)
        else:
            return render_template('gdcal.html')
    return render_template('cal.html')


if __name__ == '__main__':
    app.run(port=5000,debug=True)