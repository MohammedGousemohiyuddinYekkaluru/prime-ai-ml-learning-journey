from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = "some secret message or key"

@app.route("/")
def hello_world():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return "<p>login page</p>"

@app.route("/contact")
def contact():
    flash("timings are from 9-5")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)