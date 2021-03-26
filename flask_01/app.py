from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route('/login', methods=('GET','POST'))
def login():
    if request.method =='GET':
        return render_template('index.html')
    elif request.method =='POST':
        log = request.form['login']
        passw = request.form['password']
        success="Zostałeś zalogowany!"
        error = "Błędne hasło!"
        if passw!="jeleń":
            return render_template('index.html',error = error,login = log)
        elif passw=="jeleń":
            return redirect('calc')
@app.route('/calc', methods = ('GET','POST',))
def example():
    if request.method=='GET':
            return render_template('calc.html')
    elif request.method=='POST':
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