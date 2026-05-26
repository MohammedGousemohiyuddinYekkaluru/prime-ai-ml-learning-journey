from flask import Flask, render_template, url_for, request 

app = Flask(__name__, static_folder="assets")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/handle-login", methods=["GET", "POST"])
def handle_login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        return f"Welcome {name}!"

if __name__ == "__main__":
    app.run(debug=True)