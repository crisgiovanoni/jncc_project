from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/churn")
def churn():
    return render_template("graph/map_churn.html")
    
if __name__ == "__main__":
    app.run(debug=True)
  We made two new changes