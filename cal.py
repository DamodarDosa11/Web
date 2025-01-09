from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def cal():
    return render_template('gdcal.html')

@app.route('/cal')
def gdc():
    return render_template('cal.html')

@app.route('/cal')
def cale():
    if request.methods == ['POST','GET']:
        n = request.form['name']
        c = request.form['code']
        p = request.form['password']
        if p == 'admin':
            return render_template('cal.html', name=n, code=c)
        else:
            return render_template('gdcal.html')
    return render_template('cal.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)