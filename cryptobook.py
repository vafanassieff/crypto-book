#! /usr/bin/env python3.6
from api.bittrex import API_Bittrex
import sys
import argparse

api = API_Bittrex('key', 'secret')

def price(args):
    if not args.market:
        args.market = 'BTC'
    if not args.exchange:
        args.exchange = 'Bittrex'

    market = '{0}-{1}'.format(args.market, args.currency)
    request = api.get_marketsummary(market)
    if not request['message']:
        price = str(request['result'][0]['Last'])
        if args.quiet:
            print(price)
        else:
            print(args.exchange, market, price + u'\u20bf')
    else:
        print(request['message'])

# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')
subparsers = parser.add_subparsers(help='Use -h with the subcommande to see the help section')

# create the parser for the "price" command
parser_price = subparsers.add_parser('price', help='Show the current price of the currency specified in currency')
parser_price.add_argument('currency', type=str, help='Currency you want to see the price default exchange in BTC')
parser_price.add_argument('-m', '--market', action='store', type=str, dest='market', nargs='?', help='Choose the market BTC ETH | default is BTC')
parser_price.add_argument('-e', '--exchange', action='store', type=str, dest='exchange', nargs='?', help='Choose the market default is Bittrex')
parser_price.add_argument('-q', '--quiet', action='store_true', help='Only the price is Ouput')
parser_price.set_defaults(function=price)

# parse some argument lists
args = parser.parse_args()

#call the function of the subparser
args.function(args)