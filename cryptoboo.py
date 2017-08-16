#! /usr/bin/env python3.6
from api.bittrex import Bittrex
import sys

api = Bittrex('key', 'secret')

if sys.argv[1] == str('price'):
    trade = 'BTC'
    currency = sys.argv[2]
    market = '{0}-{1}'.format(trade, currency)
    marketsummary = api.get_marketsummary(market)
    print(marketsummary['result'][0]['Last'], u'\u20bf')