from flask import Flask,redirect,url_for,render_template,request
from flask.globals import session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
users = {}

@app.route("/")
def index():
    return redirect(url_for('hello',username='nieznajomy'))


@app.route('/<username>')
def hello(username):
    if 'login' in session:
        return render_template('hello.html',username = username)
    else:
        return "Error"


@app.route('/login',methods=['POST','GET',])
def login():
    if request.method=="POST":
        username = request.form['login']
        if username in users:
            session['login']='username'
            return redirect(url_for('hello',username=username))
    return render_template('login.html')
@app.route('/register',methods=["POST","GET",])
def form():
    if request.method=='POST':
        error = "Zostałeś zarejestrowany poprawnie!"
        login = request.form['login']
        password = request.form['password']
        acc_password = request.form['acc_password']
        if len(login)>16 or len(login)<4:
            error="Niepoprawny login, sprawdź długość znaków. (4-16)"
        elif acc_password!=password:
            error="Podane hasła nie są takie same."
        else:
            users[login]=password
    else:
        error= None
    return render_template('register_form.html',error = error)
if __name__ == '__main__':
    app.run(debug=True)