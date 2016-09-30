from flask import Flask, render_template, request
app = Flask(__name__)    #create Flask object


@app.route("/")
def disp_loginpage():
    print "\n\n\n"
    print "***DIAG: this Flask obj ***"
    print app
    print "***DIAG: request obj ***"
    print request
    print "***DIAG: request.args ***"
    print request.args
    print "***DIAG: request.args['username']  ***"
    #print request.args['username'] #only works if username submitted
    #print "***DIAG: request.headers ***"
    #print request.headers          #only works for POST
    return render_template( 'login.html' )


@app.route("/auth", methods=['POST'])
def authenticate():
    username = "morty"
    password = "wubba"
    inputtedUser = request.form['username']
    inputtedPass = request.form['password']
    if username == inputtedUser and password == inputtedPass:
        my_title = "Get ready to enter the void!"
        my_text = "Yes, you did it."
    else:
        my_title = "You are a failure."
        my_text = "Come on Morty, you gotta get schwifty."

    return render_template("success.html", title = my_title, text = my_text)

    


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
