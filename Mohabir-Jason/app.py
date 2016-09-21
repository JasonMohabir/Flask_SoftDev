#Jason Mohabir
#SoftDev pd8
#HW02 -- Fill Your Flask
#2016-09-21

from flask import Flask, render_template
app = Flask(__name__)

coll = ["Genesis", "Exodus"]

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/Heidegger")
def beingandtime():
    return "Dasnitch"

@app.route("/Camus")
def stranger():
    return "I opened myself to the gentle indifference of the world."

@app.route("/Sartre")
def noexist():
    return "Man is condemned to be free; because once thrown into the world, he is responsible for everything he does."

@app.route("/my_first_template")
def test_template():
    return render_template("foo.html", foo = "Apple", fool = coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
