from flask  import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key="06yfvpp214rf-a724"

@app.route('/login' , methods = ('GET','POST',))
def login():
    if request.method=='POST':
        username = request.form['login']
        password = request.form['password']
        if password =='banan':
            session['username'] = username
            return redirect(url_for('home'))
        return render_template('login.html', error = "Błędne hasło!", user=username)
    return render_template('login.html')
@app.route('/home')
def home():
    if session:
        return render_template('index.html',username=session['username'])
    return redirect('login')

@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)