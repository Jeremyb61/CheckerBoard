from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def checker():
    return render_template("checker.html")

@app.route("/<x>/<y>")
def xy(x,y):
    return render_template("checker.html", x=int(x), y=int(y) )
    


if __name__=="__main__":
    app.run(debug=True)