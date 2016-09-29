
import job # Occupation Selector
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def redir():
    return redirect("/occupations")

@app.route("/occupations")
def occupations():
    raw_data = job.parseCSV("occupations.csv")
    return render_template(
        "app3.html",
        title="Occupation Randomizer",
        occupation=job.pickOccupation(raw_data),
        data=raw_data
    )

if (__name__ == "__main__"):
    app.debug = True # Debugging
    app.run() # Start
    
