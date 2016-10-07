from flask import Flask, render_template, request, session
import hashlib
import csv
app = Flask(__name__)    #create Flask object


@app.route("/")
def index():
    if session.has_key('username'):
        return redirect(url_for("welcome"))
    else:
        return redirect(url_for("home")))


@app.route("/welcome", methods=["POST"])
def welcome():
    if not session.has_key('user'):
        return "You are not logged in!"
    return render_template("success.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/auth", methods=["POST"])
def disp_loginpage():
    if (userinput in users):
        if (users[userinput] == passHash):
            session['username'] = userinput
            return redirect(url_for("welcome"))
        return render_template("auth.html", cond ="Incorrect password.")
    return render_template("auth.html", cond ="Account not found.")
    return render_template("login.html")



@app.route("/auth", methods=['POST'])
def authenticate():
    inputtedUser = request.form['username']
    inputtedPass = request.form['password']
    inputtedTask = request.form['task']

    if inputtedTask == "register":

        accountInfo = csv.reader(open("data/info.csv"))
        for i in accountInfo:
            if inputtedUser == i[0]:
                return render_template("fail.html",
                                       title = "Failed Login", 
                                       text = "This username is already registered!")

        hashPass = hashlib.sha1()
        hashPass.update(inputtedPass)
        newInfo = inputtedUser + "," + hashPass.hexdigest()
        newLine = open("data/info.csv","a")
        newLine.write(newInfo)
        newLine.close

        return render_template("success.html",
                               title = "Account Creation Successful",
                               text = "A new account has been created for the user: " + inputtedUser)

    if inputtedTask == "login":
        accountInfo = csv.reader(open("data/info.csv"))
        for i in accountInfo:
            if inputtedUser == i[0]:
                hashPass = hashlib.sha1()
                hashPass.update(inputtedPass)
                if i[1] == hashPass.hexdigest():
                    return render_template("success.html", 
                                           title = "Welcome to the Promise Land",
                                           text = "You have logged in successfully. Welcome: " + inputtedUser)
                else:
                    return render_template("fail.html",
                                           title = "Failed Login",
                                           text = "Your username or password were incorrect")
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()