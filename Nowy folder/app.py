import os
from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)
ROOT_DIRECTORY = ""
x={1:1,2:2}
@app.route('/<path:directory>')
def render_listining(directory):
    ls=os.listdir(directory)
    ls_directory=[]
    ls_file=[]
    for x in ls:
        if os.path.isdir(x):
            ls_directory.append({"url":x,"name":x})
        else:
            ls_directory.append(x)
    return render_template("index.html",ls_directory=ls_directory,ls_file=ls_file,directory=directory)
@app.route("/")
def root():
    directory=""
    if directory=="":
        directory=os.listdir(ROOT_DIRECTORY)
    return render_listining(directory)

if __name__ == '__main__':
    app.run(debug=True)