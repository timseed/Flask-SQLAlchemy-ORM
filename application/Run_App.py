from application.database import *
from application.server import app
# This is needed for the Db Create
from application.models import user


with app.test_request_context():

    """ Auto Remove Db Session when the App ends"""
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        print("Session Shutdown fired")
        db_session.remove()
    Base.metadata.create_all(engine)
    app.run()





