from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/users")
def users():
    return render_template("users.html")

@app.route("/add")
def add_user():
    return render_template("add_user.html")

if __name__ == "__main__":
    app.run(debug=True)