from flask import Flask, render_template, request, redirect, url_for, session
from utils import Helper
import os
import csv
app = Flask(__name__)
app.secret_key = "secretKey"

loginIssue = ""
registerIssue = ""

@app.route("/")
def start():
    if session.has_key('user'):
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('home'))

@app.route("/welcome")
def welcome():
    if not session.has_key('user'):
        return "Go away"
    return render_template("Welcome.html", user = session['user'])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('start'))

@app.route("/home")
def home():
    return render_template("Home.html")

@app.route("/login")
def login():
    global loginIssue
    tempmessage = loginIssue
    loginIssue = ""
    return render_template("Login.html", message = tempmessage)


@app.route("/auth", methods=['POST','GET'])
def authenticate():
    global loginIssue
    username = request.form['username']
    password = request.form['password']

    mydict = Helper.CSVtoDict('static/data.csv')
        
    if username not in mydict.keys():
        loginIssue = "Sorry, username does not exist"
        return redirect(url_for("login"))
    
    if not Helper.isMatch(mydict[username], password):
        loginIssue = "Incorrect password"
        return redirect(url_for("login"))

    session['user'] = username
    return redirect(url_for("welcome"))


@app.route("/register")
def register():
    global registerIssue
    tempmessage = registerIssue
    registerIssue = ""
    return render_template("Register.html", message = "")


@app.route("/regauth", methods = ['POST','GET'])
def regauthenticate():
    global loginIssue
    global registerIssue
    username = request.form['username']
    filepath = 'static/data.csv'
    
    mydict = Helper.CSVtoDict(filepath)
        
    for key, value in mydict.items():
        if key == username:
            registerIssue = "Username already exists"
            return redirect(url_for("register"))

    Helper.addUser(filepath, username, request.form['password'])

    lmessage = "Registration successful! Please log in."
    return redirect(url_for("login"))
 

if __name__ == "__main__":
    app.debug = True
    app.run()
