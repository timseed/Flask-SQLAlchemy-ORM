import daiquiri
from flask import request, abort
from flask_restful import Resource
from application.server import api


userRESTData= {'1': {"name": "bob", "desc": "Programmer"},
               '2': {"name": "mary", "desc": "Dba"},
               '3': {"name": "ahmed", "desc": "Network"}}


class UserRESTAPI(Resource):

    def __init__(self):
        self.logger = daiquiri.getLogger(__name__)
        self.logger.debug("{} being Invoked".format(__name__))

    def get(self, userId):
        print("UserRESTAPI Hit")
        if userId in userRESTData.keys():
            return {userId: userRESTData[userId]}
        else:
            abort(404)

    def put(self, todo_id):
        #To Do
        return request("Ok")


api.add_resource(UserRESTAPI, '/REST/<string:userId>')