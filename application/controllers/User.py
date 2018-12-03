class User():

    def __init__(self,app):
        print("Applying {} route".format(__name__))

        @app.route('/user/')
        def hellouser():
            return "Hello from Users!"
