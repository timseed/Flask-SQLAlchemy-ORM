from application.database import db
from application.server import app
from application.controllers import default_route, User
db.init_app(app)
# For Each Route - Add the Initializer here
default_route(app)
User(app)
