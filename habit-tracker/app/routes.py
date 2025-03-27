
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db  # Import the CS50 SQL connection
import datetime

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
    if "user_id" not in session:
        flash("Please log in first.", "danger")
        return redirect(url_for("auth.login"))
    
    # Get today's date and compute the current week (Monday to Sunday)
    today_date = datetime.date.today()
    today = today_date.isoformat()
    start_of_week = (today_date - datetime.timedelta(days=today_date.weekday())).isoformat()
    end_of_week = (today_date - datetime.timedelta(days=today_date.weekday()) + datetime.timedelta(days=6)).isoformat()
    
    # Retrieve all habits for the logged-in user
    habits = db.execute("SELECT * FROM habits WHERE user_id = ?", session["user_id"])
    
    # For each habit, check if it's been completed:
    for habit in habits:
        freq = habit["frequency"].lower()
        if freq == "daily":
            # Check if there's a completion record for today
            comp = db.execute("SELECT * FROM completions WHERE habit_id = ? AND user_id = ? AND date_completed = ?", 
                              habit["id"], session["user_id"], today)
            habit["completed"] = len(comp) > 0
        elif freq == "weekly":
            # Check if a completion record exists for this habit within the current week
            comp = db.execute("SELECT * FROM completions WHERE habit_id = ? AND user_id = ? AND date_completed BETWEEN ? AND ?", 
                              habit["id"], session["user_id"], start_of_week, end_of_week)
            habit["completed"] = len(comp) > 0
        else:
            habit["completed"] = False

    # Separate habits by frequency
    daily_habits = [h for h in habits if h["frequency"].lower() == "daily"]
    weekly_habits = [h for h in habits if h["frequency"].lower() == "weekly"]
    
    return render_template("dashboard.html", daily_habits=daily_habits, weekly_habits=weekly_habits)

@main.route("/complete-habit/<int:habit_id>", methods=["POST"])
def complete_habit(habit_id):
    if "user_id" not in session:
        flash("Please log in first.", "danger")
        return redirect(url_for("auth.login"))
    
    today = datetime.date.today().isoformat()
    # Check if this habit is already marked as completed for today (for daily) 
    # or for the current week (for weekly)
    habit_rows = db.execute("SELECT frequency FROM habits WHERE id = ? AND user_id = ?", habit_id, session["user_id"])
    if not habit_rows:
        flash("Habit not found.", "danger")
        return redirect(url_for("main.dashboard"))
    
    frequency = habit_rows[0]["frequency"].lower()
    if frequency == "daily":
        existing = db.execute("SELECT * FROM completions WHERE habit_id = ? AND user_id = ? AND date_completed = ?", 
                              habit_id, session["user_id"], today)
    elif frequency == "weekly":
        # For weekly, check if there's any record in the current week
        today_date = datetime.date.today()
        start_of_week = (today_date - datetime.timedelta(days=today_date.weekday())).isoformat()
        end_of_week = (today_date - datetime.timedelta(days=today_date.weekday()) + datetime.timedelta(days=6)).isoformat()
        existing = db.execute("SELECT * FROM completions WHERE habit_id = ? AND user_id = ? AND date_completed BETWEEN ? AND ?", 
                              habit_id, session["user_id"], start_of_week, end_of_week)
    else:
        existing = []
    
    if existing:
        flash("This habit is already marked as completed.", "info")
    else:
        db.execute("INSERT INTO completions (habit_id, user_id, date_completed) VALUES(?, ?, ?)", 
                   habit_id, session["user_id"], today)
        flash("Habit marked as completed!", "success")
    return redirect(url_for("main.dashboard"))

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

@main.route("/habits")
def habits():
    if "user_id" not in session:
        flash("Please log in first.", "danger")
        return redirect(url_for("auth.login"))
    
    # Query the habits for the current user
    habits = db.execute("SELECT * FROM habits WHERE user_id = ?", session["user_id"])
    return render_template("habits.html", habits=habits)

    
@main.route("/delete-habit/<int:habit_id>", methods=["POST"])
def delete_habit(habit_id):
    if "user_id" not in session:
        flash("Please log in first.", "danger")
        return redirect(url_for("auth.login"))
    
    # Delete the habit only if it belongs to the current user
    db.execute("DELETE FROM habits WHERE id = ? AND user_id = ?", habit_id, session["user_id"])
    flash("Habit deleted successfully!", "success")
    return redirect(url_for("main.habits"))