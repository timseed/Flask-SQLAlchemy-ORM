class User_route():

    def __init__(self,app):
        print("Applying /user/ route")

        @app.route('/user/')
        def hellouser():
            return "Hello from Users!"
