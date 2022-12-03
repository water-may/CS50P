#! /usr/bin/python3.10

import sys
import requests
import json 

def main(): 
    dat = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = float(dat.json()["bpi"]["USD"]["rate"].replace(",", ""))
    amount = rate * inp()
    print(f"${amount:,.4f}")
    

def inp():
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")

main()