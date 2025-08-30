import os

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, select, or_, func
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = os.getenv("FLASH_SECRET_KEY")  # use a secure value in real apps

# Choose DB per environment
db_uri = os.getenv("DATABASE_URL")
if os.getenv("FLASK_ENV") == "test":  # only set in pytest
    db_uri = os.getenv("TEST_DATABASE_URL")

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # recommended off in 2.x

# Create database handle
db = SQLAlchemy(app)

# Model for Users table
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))


# Test DB connection
@app.route("/test-db")
def test_db():
    try:
        db.session.execute(text("SELECT 1"))
        return "Database connected successfully with SQLAlchemy!"
    except Exception as e:
        return f"Database connection failed: {e}"


# Welcome page
@app.route("/")
def welcome():
    return render_template("welcome.html")


# Show all users (with search)
@app.route("/users")
def users():
    query = request.args.get("query", "").strip()
    stmt = select(User)
    if query:
        stmt = stmt.where(
            or_(
                User.name.ilike(f"%{query}%"),
                User.email.ilike(f"%{query}%"),
                User.phone.ilike(f"%{query}%"),
                User.department.ilike(f"%{query}%"),
            )
        )
    results = db.session.execute(stmt).scalars().all()
    return render_template("users.html", users=results)


# Add new user
@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        department = request.form["department"].strip()

        stmt = select(User).where(func.lower(User.email) == email.lower())
        existing_user = db.session.execute(stmt).scalar_one_or_none()

        if existing_user:
            flash("A user with this email already exists!", "error")
            return redirect(url_for("add_user"))

        user = User(name=name, email=email, phone=phone, department=department)
        db.session.add(user)
        db.session.commit()
        flash("User added successfully!", "success")
        return redirect(url_for("users"))

    return render_template("add_user.html")


# Update user
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    user = db.session.get(User, id) or abort(404)

    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        department = request.form["department"].strip()

        stmt = select(User).where(func.lower(User.email) == email.lower(), User.id != id)
        duplicate = db.session.execute(stmt).scalar_one_or_none()

        if duplicate:
            flash("A user with this email already exists!", "error")
            return redirect(url_for("update_user", id=id))

        user.name = name
        user.email = email
        user.phone = phone
        user.department = department
        db.session.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for("users"))

    return render_template("update_user.html", user=user)


# Confirm updated user (preview page)
@app.route("/update/confirm/<int:id>", methods=["POST"])
def confirm_update_user(id):
    user = db.session.get(User, id) or abort(404)
    return render_template(
        "confirm_update.html",
        user=user,
        name=request.form["name"],
        email=request.form["email"],
        phone=request.form["phone"],
        department=request.form["department"],
    )


# Delete user
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete_user(id):
    user = db.session.get(User, id) or abort(404)
    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully!", "success")
        return redirect(url_for("users"))
    return render_template("delete_user.html", user=user)


# Run the app
if __name__ == "__main__":
    app.run()