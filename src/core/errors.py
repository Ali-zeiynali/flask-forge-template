from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"error": "not found"}), 404
