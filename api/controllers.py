# from flask_restplus import Namespace, Resource, fields
# from flask import request

# play_api = Namespace('transaction', description='Api for dealing with every transaction happening in gtg')


# @play_api.route('/play')
# class PeopleData(Resource):

#     def get(self):
#         """
#             HTTP method to create a new buyer
#             @param: buyer_id: ID of the buyer
#             @returns: response and status code
#         """
#         data = request.values.to_dict() or ''
#         payload = api.payload or data
#         schema = NewBuyerSchema(strict=True)
#         response = {}
        
#         try:
#             new_payload = schema.load(payload).data
#         except (Exception, ValidationError) as e :
#             logger.exception(e)
#             response = {}
#             response['success'] = False
#             response['errors'] = "You need to pass in a payload"
#             return response, 400

        