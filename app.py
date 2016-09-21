#Jason Mohabir
#SoftDev pd8
#HW02 -- Fill Your Flask
#2016-09-21

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"
    

@app.route("/Camus")
def stranger():
    return "I opened myself to the gentle indifference of the world."

@app.route("/Sartre")
def noexist():
    return "Man is condemned to be free; because once thrown into the world, he is responsible for everything he does."

if __name__ == "__main__":
    app.run()
