from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc', methods=('GET', 'POST',))
def example():
    if request.method == 'GET':
        return render_template('calc.html')
    elif request.method == 'POST':
        a = float(request.args.get('a', default="1", type=int))
        b = float(request.form['b'])
        sign = str(request.form['sign'])
        return redirect(url_for('result', sign=sign, a=a, b=b))


@app.route('/calc/<string:sign>/<float:a>/<float:b>')
def result(sign, a, b):
    a = a
    b = b
    sign = sign
    if sign == "dodawanie":
        wynik = a+b
    elif sign == "odejmowanie":
        wynik = a-b
    elif sign == "mnozenie":
        wynik = a*b
    elif sign == "dzielenie":
        wynik = a/b
    return render_template('calc.html', wynik=wynik)


@app.route('/users', methods=('GET', 'POST',))
def users():
    if request.method == "POST":
        id = int(request.form['id'])
        return redirect(url_for('users_result', user_id=id))
    else:
        return render_template('users.html')


@app.route('/users/<int:user_id>')
def users_result(user_id):
    class User:
        def __init__(self, id, nick, register_date, post_n):
            self.id = id
            self.nick = nick
            self.register_date = register_date
            self.post_n = post_n

        def info(self):
            return "Id: " + self.id + '\nNick: ' + self.nick + "\nregister date: " + self.register_date + "\nnumber of posts: " + self.post_n
    user1 = User("1", "max2332", "06.03.2001", "50")
    user2 = User("2", "ralf12", "02.04.2011", "1")
    user3 = User("3", "XXBody11", "02.05.2021", "1520")
    users_list = [user1, user2, user3]
    if user_id > len(users_list):
        info = "User with that ID dont exist!"
    else:
        info = users_list[user_id-1].info()
    return render_template('users.html', user_info=info)


if __name__ == '__main__':
    app.run(debug=True)
