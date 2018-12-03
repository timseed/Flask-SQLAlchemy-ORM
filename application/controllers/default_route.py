
class default_route():

    def __init__(self,app):
        print("Applying / route")

        @app.route('/')
        def hellodefault():
            return "Hello default!"
