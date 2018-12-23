# from flask_restplus import Namespace, Resource, fields
# from flask import request
# from api import api
# from schema import NewPersonSchema

# play_api = Namespace('transaction', description='Api for dealing with every transaction happening in gtg')


# people = play_api.model('people', {
#     'id': fields.String(required=True, description='The name of the facility'),
#     'name': fields.String(description='The facility address'),
#     'time': fields.String(description='time transaction occured')
# })

# incomes = [
#   { 'description': 'salary', 'amount': 5000 }
# ]

# @account_api.route('/credit/')
# class People(Resource):
# 	"""
# 		Api to credit a user's account
# 	"""

# 	@account_api.expect(credit)  # For swagger documentation
# 	def post(self):
# 		"""
# 			HTTP method for making account credits
# 			@param: request payload
# 			@returns: response and status code
# 		"""
# 		schema = NewPersonSchema(strict=True)
# 		data = request.values.to_dict()
# 		payload = api.payload or data
# 		print('Payload', payload)

# 		response = {}

#         try:
# 			people_payload = schema.load(payload).data._asdict()
# 			print('People payload',people_payload)
# 		except Exception as e:
# 			print('payload',payload)
# 			# logger.exception(e.messages)
# 			response['success'] = False
# 			response['message'] = e.messages
# 			return response, 400
            

# # @play_api.route('/incomes')
# # class Activate(Resource)
# #     def get(self):
# #         return jsonify(incomes)


# # @play_api.route('/incomes', methods=['POST'])
# # def add_income():
# #   incomes.append(request.get_json())
# #   return '', 204