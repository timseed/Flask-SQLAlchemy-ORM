from flask import Flask
import os
app = Flask(__name__)
path = os.path.dirname( os.path.realpath(__file__) )
database_path = os.path.join(path, '../db/mydb.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path