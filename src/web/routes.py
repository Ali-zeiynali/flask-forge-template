from flask import Blueprint, current_app, render_template

web_bp = Blueprint("web", __name__, template_folder="templates", static_folder="static")


@web_bp.get("/")
def index():
    database_uri = current_app.config.get("SQLALCHEMY_DATABASE_URI", "unknown")
    database_engine = (
        database_uri.split(":", maxsplit=1)[0] if ":" in database_uri else database_uri
    )
    status_cards = {
        "Environment": current_app.config.get("FLASK_ENV", "development"),
        "Version": current_app.config.get("APP_VERSION", "0.1.0"),
        "Database": database_engine,
        "Auth Mode": "JWT + RBAC",
        "CI Status": current_app.config.get("CI_STATUS", "Configured"),
    }
    return render_template(
        "index.html",
        status_cards=status_cards,
        docs_url=current_app.config.get("DOCS_URL", "/docs/index.md"),
        github_url=current_app.config.get(
            "GITHUB_URL", "https://github.com/Ali-zeiynali/flask-forge-template"
        ),
    )
