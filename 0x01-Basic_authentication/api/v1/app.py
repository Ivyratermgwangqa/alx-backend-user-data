#!/usr/bin/env python3
"""
Flask application setup module.
"""

from flask import Flask, jsonify, request, abort
from api.v1.views.index import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
import os

app = Flask(__name__)
app.register_blueprint(app_views)

auth = None
AUTH_TYPE = os.getenv('AUTH_TYPE')

if AUTH_TYPE == 'auth':
    auth = Auth()
elif AUTH_TYPE == 'basic_auth':
    auth = BasicAuth()

@app.before_request
def before_request():
    """
    Function to handle authentication before each request.
    """
    if auth is None:
        pass
    else:
        if auth.require_auth(request.path, ['/api/v1/status/',
                                            '/api/v1/unauthorized/',
                                            '/api/v1/forbidden/']):
            if auth.authorization_header(request) is None:
                abort(401)
            if auth.current_user(request) is None:
                abort(403)

@app.errorhandler(401)
def unauthorized(error):
    """
    Error handler for 401 Unauthorized error.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    """
    Error handler for 403 Forbidden error.
    """
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    app.run(host=os.getenv('API_HOST', '0.0.0.0'), port=os.getenv('API_PORT', '5000'))
