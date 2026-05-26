from flask import Flask, render_template, url_for, request 

app = Flask(__name__, static_folder="assets")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        return f"<p>Welcome {name}!</p>"
    
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)