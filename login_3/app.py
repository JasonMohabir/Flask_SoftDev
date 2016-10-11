# Flask App for Forms

from flask import Flask, render_template, redirect, request, session, url_for
from utils import authenticate
app = Flask(__name__)

app.secret_key = "This is probably a really bad idea!"


@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("auth"))

@app.route("/login", methods=["POST", "GET"]) 
def auth():
    try:
        if "user" in session:
            return redirect(url_for("welcome"))
        action = request.form["action"]
    except:
        return render_template("form.html")
    if action == "Login":
        return login(request.form["username"],request.form["password"])
    if action == "Register":
        return register(request.form["username"],request.form["password"])

@app.route("/logout", methods=["POST"])
def quit():
    return logout()

@app.route("/welcome", methods=["POST", "GET"])
def welcome():
    return render_template("welcome.html")
        
def login(username,password):
    logstatus = authenticate.verify(username,password)
    if logstatus > 0:
        session["user"] = username
        return render_template("welcome.html")
    elif logstatus == -1:
        return render_template("form.html",
                               status="Login Failed: Invalid password.")
    elif logstatus == -2:
        return render_template("form.html",
                               status="Login Failed: User does not exist.")

def register(username,password):
    regstatus = authenticate.register(username,password)
    if regstatus > 0:
        return render_template("form.html",
                               status="Registration Success!")                    
    elif regstatus == -1:
        return render_template("form.html", 
                               status="Registration Failed: Username already exists.")                    

def logout(username):
    session.pop("user")
    return render_template("form.html",
                           status="You have been logged out!")


if __name__ == "__main__":
    app.debug = True
    app.run()
