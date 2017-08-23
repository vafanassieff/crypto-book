import sys
import json
from api.bittrex import API_Bittrex

api = API_Bittrex('key', 'secret')

def get_last_price(args):

	market = get_market(args)
	request = api.get_marketsummary(market)
	if not request['message']:
		last = str(request['result'][0]['Last'])
		return (last)
	else:
		print(request['message'])
		sys.exit(0)

def get_market(args):

	if not args.market:
		args.market = 'BTC'
	return (args.market + '-' + str.upper(args.currency))

def get_exchange(args):

	if not args.exchange:
		return ('Bittrex')
	return (args.exchange)

def	get_id():
    
	path = './book.json'
	data = json.loads(open(path).read())
	if len(data) == 0:
		return 0
	order_id = data[len(data) - 1]['id']
	order_id += 1
	return order_id