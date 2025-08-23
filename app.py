from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

app = Flask(__name__)

# Get variables from env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# Database connection 
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# Create database 
db = SQLAlchemy(app)


# Model for Users table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))

# TestDB connection
@app.route("/test-db")
def test_db():
    try:
        # Simple query to test connection
        db.session.execute(text("SELECT 1"))
        return "Database connected successfully with SQLAlchemy!"
    except Exception as e:
        return f"Database connection failed: {e}"



# Welcome page
@app.route("/")
def welcome():
    return render_template("welcome.html")

# Show all users
@app.route("/users")
def users():
    all_users = User.query.all()
    return render_template("users.html", users=all_users)

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