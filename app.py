from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/portofolio")
def portofolio():
    return render_template("portofolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
