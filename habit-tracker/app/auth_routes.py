# app/auth_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db  # Import our cs50 database connection

auth = Blueprint("auth", __name__)

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
            flash("Passwords do not match!", "danger")
            return redirect(url_for("auth.register"))

        # Check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0:
            flash("Username already taken!", "danger")
            return redirect(url_for("auth.register"))

        # Hash the password and insert the new user into the database
        hashed = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashed)
        
        # Retrieve the user id and store it in session
        rows = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]

        flash("Registration successful!", "success")
        return redirect(url_for("main.home"))

    return render_template("register.html")
