import daiquiri
class default_route():

    def __init__(self,app):
        self.logger = daiquiri.getLogger(__name__)
        self.logger.debug("Applying / route")

        @app.route('/')
        def hellodefault():
            self.logger.debug("hellodefault Triggered")
            return "Hello default!"
