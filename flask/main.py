from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h2>Hello! World</h2>"

@app.route("/login")
def login_page():
    return "<p>This is login page</p>"

if __name__ == "__main__":
    app.run(debug=True)