from application.database import db
from application.server import app
from application.controllers import default_route, User
# Restful API  - should be on the Previous Line
from application.controllers import UserRESTAPI
db.init_app(app)
# For Each Route - Add the Initializer here
default_route(app)
User(app)

