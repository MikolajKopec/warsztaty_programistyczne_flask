from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route('/',methods=('GET','POST',))
def index():
    return render_template('index.html')
@app.route('/login', methods=('GET','POST'))
def login():
    passw=""
    log = request.form['login']
    passw = request.form['password']
    success="Zostałeś zalogowany!"
    error = "Błędne hasło!"
    if passw!="jeleń":
        return render_template('index.html',error = error,login = log)
    elif passw=="jeleń":
        return redirect('calc')
@app.route('/calc', methods = ('GET','POST',))
def calc():
    return render_template('calc.html')
@app.route('/calc_value', methods = ('GET','POST',))
def example():
    a = float(request.form['a'])
    b = float(request.form['b'])
    s = request.form['sign']
    if s=="+":
        wynik = a+b
    elif s=="-":
        wynik = a-b
    elif s=="*":
        wynik = a*b
    elif s=="/":
        wynik = a/b
    return render_template('calc.html', wynik = wynik)
if __name__ == '__main__':
    app.run(debug=True)