"""
This is a Sub for the Global Db Object

This object is used in

   - Models
   - create_database
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from application.server import app


db = SQLAlchemy()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
