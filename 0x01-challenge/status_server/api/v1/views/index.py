#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views


# /api/v1/status was changed to /status
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
