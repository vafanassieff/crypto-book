import sys
import json
from api.bittrex import API_Bittrex
from colr import color

api = API_Bittrex('key', 'secret')

def get_last_price_tmp(market):
	"""Return the last price using the market"""
	request = api.get_ticker(market)
	if not request['message']:
		last = str(request['result']['Last'])
		return (last)
	else:
		print(request['message'])
		sys.exit(0)

def get_last_price(args):
	"""Return the last price using args"""
	market = get_market(args)
	request = api.get_ticker(market)
	if not request['message']:
		last = str(request['result']['Last'])
		return (last)
	else:
		print(request['message'])
		sys.exit(0)

def get_market(args):
	"""Return the market"""
	if not args.market:
		args.market = 'BTC'
	return (args.market + '-' + str.upper(args.currency))

def get_exchange(args):
	"""Return the exchange"""
	if not args.exchange:
		return ('Bittrex')
	return ('Bittrex')

def	get_id():
	"""Return the next id to append the book.json"""
	path = './book.json'
	data = json.loads(open(path).read())
	if len(data) == 0:
		return 0
	order_id = data[len(data) - 1]['id']
	order_id += 1
	return order_id

def get_profit(buying_price, current):
	"""Compute the variation since the order was placed"""
	variation = 100 * (float(current) - float(buying_price)) / float(buying_price)
	if variation > 0:
		variation = '+' + str(round(variation, 2)) + '%'
		variation = color(variation, fore='green')
	else:
		variation = str(round(variation, 2)) + '%'
		variation = color(variation, fore='red')
	return variation