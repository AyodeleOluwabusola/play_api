from flask_restplus import Namespace, Resource, fields
from flask import request

class MyResourceClass(Resource):

    def get(self, id=None):
        if not id:
    # item ID was not provided over get method
            return 404
    # Do stuff
        return 200

    # def post(self):
    ## Should accept JSON
    ## Does some stuff based on request
    def delete(self):
    ## Deletes the item information
        return 200

