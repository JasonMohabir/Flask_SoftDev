#Jason Mohabir
#SoftDev1 pd8
#HW03 -- ...and Now Enjoy its Contents
#2016-09-23

from flask import Flask, render_template, redirect
import random

app = Flask(__name__)

occL = open("occupations.csv").read();
occL = occL.split('\n')
lineZero = occL[0]
del occL[0]
lineLast = occL[len(occL)-1]
del occL[len(occL)-1]

occDict = {}
upperBoundL = []
currentUpperBound = 0
occL2 = []

for line in occL:
    occL2.append(line.rsplit(",",1))
    occS = line.rsplit(",",1)[0]
    currentUpperBound += float(line.rsplit(",",1)[1])
    occDict[currentUpperBound] = occS
    upperBoundL.append(currentUpperBound)
    
def pickOccupation():
    randNum = random.random()*99.8
    passenger = 0
    for line in occL2:
        percentage = float(line[1])
        passenger+=percentage
        if randNum < passenger:
            return line[0]

@app.route("/")
def redir():
    return redirect("/occupations")

@app.route("/occupations")
def occTable():
    return render_template("occTable.html",occList=occL2,occupation=pickOccupation())

if __name__ == "__main__":
    app.debug = True
    app.run()
