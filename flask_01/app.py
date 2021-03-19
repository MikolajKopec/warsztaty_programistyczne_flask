from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/example', methods = ('GET','POST',))
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
    return str(wynik)
if __name__ == '__main__':
    app.run(debug=True)