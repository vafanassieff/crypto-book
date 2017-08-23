from function.function import *
import time
import json

class Order:
    
	def __init__(self, args):
		self.id = get_id()
		self.last = get_last_price(args)
		self.time = time.strftime("%c")
		self.market = get_market(args)
		self.exchange = get_exchange(args)

	def toJSON(self):
		return json.dumps(self.__dict__, sort_keys=False)

	def toDict(self):
		return (self.__dict__)
