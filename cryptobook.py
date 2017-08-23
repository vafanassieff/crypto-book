#! /usr/bin/env python3.6
import sys
import argparse
import os
import time
import json
from terminaltables import SingleTable
from function.function import *
from classes.order import Order

def price(args):
    
	price = get_last_price(args)
	if not price:
		return
	if args.quiet:
		print(price)
	else:
		print(get_exchange(args), get_market(args), price + u'\u20bf')

def buy(args):
    
	path = './book.json'
	# Check if the file book.json exist and if not create it
	# and iniate it with '[]'
	if not os.path.isfile(path):
		data = "[]"
		file = open(path, 'a+')
		file.write(data)
		file.close()
	order = Order(args)
	data = json.loads(open(path).read())
	data.append(order.toDict())
	with open('./book.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)

	# Display the order with a nice table
	table_data = [
    	['id', 'Exchange', 'Market', 'Price'],
    	[order.id , order.exchange, order.market, order.last]
	]
	table = SingleTable(table_data)
	table.title = 'Buy Order'
	print (table.table)

def main(args):

    if hasattr(args, 'function'):
    	args.function(args)

if __name__ == '__main__':

# Create the top-level parser
	parser = argparse.ArgumentParser(prog='Cryptobook')

	parser.add_argument('--version',
						action='version',
						version='%(prog)s 0.0.1')

# Creat subparser for the Price command
	subparsers = parser.add_subparsers(help='Use -h with the subcommande to see the help section')

# Create the parser for the "price" command
	parser_price = subparsers.add_parser('price',
										help='Show the current price of the currency specified in currency')
	parser_price.add_argument('currency', 
										type=str,
										help='Currency you want to see the price default exchange in BTC')

	parser_price.add_argument('-m', '--market',
										action='store',
										type=str,
										dest='market',
										nargs='?',
										choices=['BTC', 'ETH', 'USDT'],
										help='Choose the market BTC ETH | default is BTC')

	parser_price.add_argument('-e', '--exchange',
										action='store',
										type=str,
										dest='exchange',
										nargs='?',
										help='Choose the market default is Bittrex')

	parser_price.add_argument('-q', '--quiet',
										action='store_true',
										help='Only price is Ouput')

	parser_price.set_defaults(function=price)

# Create the parser for the "buy" command
	parser_buy = subparsers.add_parser('buy',
										help='Show the current price of the currency specified in currency')
	
	parser_buy.add_argument('currency',
										type=str,
										help='Currency you want to see the price default exchange in BTC')

	parser_buy.add_argument('-m', '--market',
										action='store',
										type=str,
										dest='market',
										nargs='?',
										choices=['BTC', 'ETH', 'USDT'],
										help='Choose the market BTC ETH | default is BTC')

	parser_buy.add_argument('-e', '--exchange',
										action='store',
										type=str,
										dest='exchange',
										nargs='?',
										help='Choose the market default is Bittrex')
	
	parser_buy.set_defaults(function=buy)

# Parse argument lists
	args = parser.parse_args()
	main(args)
