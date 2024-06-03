#!/usr/bin/env python3
"""
Index views module.
"""

from flask import Blueprint, jsonify, abort

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """
    Returns the status of the API.
    """
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """
    Endpoint to trigger a 401 error.
    """
    abort(401)

@app_views.route('/api/v1/forbidden', methods=['GET'])
def forbidden():
    """
    Endpoint to trigger a 403 error.
    """
    abort(403)
