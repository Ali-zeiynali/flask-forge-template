from flask import jsonify


def ok(payload: dict):
    return jsonify(payload), 200
