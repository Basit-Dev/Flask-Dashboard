from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = os.getenv("FLASH_SECRET_KEY")  # use a secure value in real apps

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
    email = db.Column(db.String(100), unique=True, nullable=False)
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
    # Search for users or show all users
    query = request.args.get("query", "").strip()
    if query:
        users = User.query.filter(
            (User.name.ilike(f"%{query}%")) |
            (User.email.ilike(f"%{query}%")) |
            (User.phone.ilike(f"%{query}%")) |
            (User.department.ilike(f"%{query}%"))
        ).all()
    else:
        users = User.query.all()
    return render_template("users.html", users=users)

# Add new user
@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        email = request.form["email"]

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("A user with this email already exists!", "error")
            return redirect(url_for("add_user")) 

        # If no duplicate, create new user
        user = User(
            name=request.form["name"],
            email=email,
            phone=request.form["phone"],
            department=request.form["department"],
        )
        db.session.add(user)
        db.session.commit()
        flash("User added successfully!", "success")
        return redirect(url_for("users"))
    return render_template("add_user.html")

# Update user
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.name = request.form["name"]
        user.email = request.form["email"]
        user.phone = request.form["phone"]
        user.department = request.form["department"]
        db.session.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for("users"))
    return render_template("update_user.html", user=user)

# Confirm updated user
@app.route("/update/confirm/<int:id>", methods=["POST"])
def confirm_update_user(id):
    user = User.query.get_or_404(id)
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    department = request.form["department"]
    return render_template(
        "confirm_update.html",
        user=user,
        name=name,
        email=email,
        phone=phone,
        department=department,
    )

# Delete user
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete_user(id):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully!", "success")
        return redirect(url_for("users"))
    return render_template("delete_user.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)