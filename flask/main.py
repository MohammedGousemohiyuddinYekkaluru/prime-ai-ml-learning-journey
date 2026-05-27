from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get("name", default= "anonymous")
    subject = request.args.get("subject")
    return render_template("index.html", name= name, subject= subject)

@app.route("/jsonAPI")
def json_API():
    data = {
        "msg": "working with json & API"
    }

    return jsonify(data)

@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        friends = ["Adam", "Bob", "charlie", "Dan"]
        header = "<header>ABC website</header>"

        return render_template("welcome.html", name=name, password=password, friends=friends, header=header)
    
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)