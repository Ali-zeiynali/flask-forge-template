from extensions.db import db


def get_session():
    return db.session
