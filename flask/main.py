from flask import Flask, render_template, url_for, request 

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get("name", default= "ananymous")
    subject = request.args.get("subject")
    return render_template("index.html", name= name, subject= subject)

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