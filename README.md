# crypto-book
Crypto-Book is a way to track and ask the price of a crypto currency in your terminal !

Only supporting Python 3.x

This is my first python app, i'm maybe not aware of python best practice.

Bittrex API with [python-bittrex](https://github.com/ericsomdahl/python-bittrex)

![Image of the app](https://raw.githubusercontent.com/vafanassieff/crypto-book/master/example/example.png)

## Install

To install use

```
git clone https://github.com/vafanassieff/crypto-book.git
pip3 install terminaltables
pip3 install colr
pip3 install blessed
```
```
./cryptobook.py
```

If you are on UNIX and lazy you can run the setup.sh
If needed edit the config.json file.

## Usage

To buy a crypto use 
```
./cryptoboo.py buy currency
```
Showing your position
```
./cryptoboo.py position -l
```
Close a position 
```
./cryptoboo.py close id
```

Order book is stored in a JSON file, see example-book.json in the example folder

## Feature

* Get the price of your crypto using price command
* Choose your market (BTC, ETH, USDT) if available
* Show your current position and profit since your opened it
* Close position to remove it from the order book
* Live view using position with -l

## In Dev

* Nice display of info
* Supporting more exchange (only Bittrex atm)

## Documention

Use the -h option for priting usage with command and subcommand

## Build with

* [terminaltables](https://github.com/Robpol86/terminaltables) - Cool table for term
* [Colr](https://github.com/welbornprod/colr) - Easy color for term
* [Blessed](https://github.com/jquast/blessed) - Used for the live view

## Disclaimer

This is my first CLI app in python, bug may be found !