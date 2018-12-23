from api.models import Bucketlist
from api.exceptions import UUIDClashError
from api.models import Buyer

class BuyerManager():
    """class for buying Operation"""
    def create_buyer(self, args):
        """
			Method to create new buyers
			@args: data payload
			@returns: a status message and status code
		"""            


        name = args['buyer_name']
        buyer_id= args['buyer_id']
        time= args['time']
        response ={}

        buyer_exists = Buyer.exists(
            buyer_name=name.upper(),
            buyer_id=buyer_id,
        )