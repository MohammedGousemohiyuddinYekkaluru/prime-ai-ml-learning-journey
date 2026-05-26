from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="assets")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)