"""
These are the Database Models that are created in the Db for the application.

This db object is created in the database/ section of the project.

"""

from application.database import db, Base


class user(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username',db.String(80), unique=True)
    password = db.Column('password',db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("User __init__ has fired")