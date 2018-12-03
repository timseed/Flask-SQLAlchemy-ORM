
import logging
import daiquiri
import yaml

logger = daiquiri.getLogger(__name__)


from application.database import *
from application.server import app
junk=1
try:
    with open(app.config['LOGGING_CONFIG'], "rt") as ofp:
        config = yaml.safe_load(ofp.read())
        logging.config.dictConfig(config)
except ValueError as err:
    logging.basicConfig(level=logging.DEBUG)
    logging.error("{:s} Unable to Open {:s} the log config file.".format(str(err),app.config['LOGGING_CONFIG']))


# The Next include is needed for the AutoDb Update on Start
from application.models import user
logging.debug("Starting App")
with app.test_request_context():
    """ Auto Remove Db Session when the App ends"""
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        logging.debug("Session Shutdown fired")
        db_session.remove()
    # ORM Check Db is in Sync in terms of Definitions
    Base.metadata.create_all(engine)
    # Flask Run App
    logging.debug("Handing over to Flask")
    app.run()





