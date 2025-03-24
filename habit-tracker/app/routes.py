
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db # Importing database and User model

main = Blueprint('main', __name__)
auth = Blueprint("auth", __name__)  # Creating a new Blueprint for authentication

@main.route('/')
def home():
    return render_template("index.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user"""
    
    # Clear any existing user session
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate form fields
        if not username or not password or not confirmation:
            flash("All fields are required!", "danger")
            return redirect(url_for("auth.register"))

        if password != confirmation:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("auth.register"))

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken!", "danger")
            return redirect(url_for("auth.register"))

        # Hash the password and store the user in the database
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Retrieve the newly created user and log them in
        session["user_id"] = new_user.id
        flash("Registration successful!", "success")

        return redirect(url_for("main.home"))

    return render_template("register.html")

@main.route("/dashboard")
def dashboard():
    # Example dashboard: show the user's habits if logged in.
    if "user_id" not in session:
        flash("Please log in first", "danger")
        return redirect(url_for("auth.login"))
    
    # Fetch habits for the logged-in user.
    habits = db.execute("SELECT * FROM habits WHERE user_id = ?", session["user_id"])
    return render_template("dashboard.html", habits=habits)

@main.route("/add-habit", methods=["GET", "POST"])
def add_habit():
    if "user_id" not in session:
        flash("Please log in to add a habit.", "danger")
        return redirect(url_for("auth.login"))
    
    if request.method == "POST":
        habit_name = request.form.get("habit_name")
        frequency = request.form.get("frequency")
        time_of_day = request.form.get("time_of_day")

        # Validate input – at a minimum, habit name is required.
        if not habit_name:
            flash("Habit name is required.", "danger")
            return redirect(url_for("main.add_habit"))
        
        # Insert the new habit into the habits table.
        db.execute(
            "INSERT INTO habits (user_id, habit_name, frequency, time_of_day) VALUES(?, ?, ?, ?)",
            session["user_id"], habit_name, frequency, time_of_day
        )
        flash("Habit added successfully!", "success")
        return redirect(url_for("main.dashboard"))
    
    # If GET request, render the add habit form.
    return render_template("add-habit.html")