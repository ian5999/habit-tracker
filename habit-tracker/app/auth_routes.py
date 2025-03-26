# app/auth_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import db  # Using your CS50 SQL connection

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username and password are required.", "danger")
            return redirect(url_for("auth.login"))
        
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            flash("Invalid username or password.", "danger")
            return redirect(url_for("auth.login"))
        
        session["user_id"] = rows[0]["id"]
        flash("Logged in successfully!", "success")
        return redirect(url_for("main.home"))
    
    # If GET, render the login form.
    return render_template("index.html")  # Or create a separate login.html if preferred

@auth.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        if not username or not password or not confirmation:
            flash("All fields are required!", "danger")
            return redirect(url_for("auth.register"))
        if password != confirmation:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("auth.register"))
        
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0:
            flash("Username already taken!", "danger")
            return redirect(url_for("auth.register"))
        
        hashed = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashed)
        rows = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]
        flash("Registered successfully!", "success")
        return redirect(url_for("main.home"))
    
    return render_template("register.html")

@auth.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.home"))
