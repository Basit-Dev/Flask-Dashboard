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

@app.route("/update")
def update_user():
    return render_template("update_user.html")

@app.route("/update/confirm")
def confirm_update():
    return render_template("confirm_update.html")

@app.route("/delete")
def delete_user():
    return render_template("delete_user.html")

if __name__ == "__main__":
    app.run(debug=True)