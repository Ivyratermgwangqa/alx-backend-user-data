#!/usr/bin/env python3
"""Flask app for user authentication service"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/", methods=["GET"])
def home():
    """Base endpoint"""
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def users():
    """Endpoint for user registration"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route("/sessions", methods=["POST"])
def login():
    """Endpoint for user login"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    return jsonify({"message": "invalid credentials"}), 401

@app.route("/sessions", methods=["DELETE"])
def logout():
    """Endpoint for user logout"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        return jsonify({"message": "not found"}), 404
    AUTH.destroy_session(user.id)
    return jsonify({"message": "logout successful"}), 200

@app.route("/profile", methods=["GET"])
def profile():
    """Endpoint for getting user profile"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        return jsonify({"message": "not found"}), 404
    return jsonify({"email": user.email}), 200

@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """Endpoint for generating reset password token"""
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        return jsonify({"message": "email not found"}), 404

@app.route("/reset_password", methods=["PUT"])
def update_password():
    """Endpoint for updating password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        return jsonify({"message": "invalid reset token"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
