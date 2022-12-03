#! /usr/bin/python3.10
import sys
import csv
from tabulate import * 

def main():
    if check():
        try:
            file = open(sys.argv[1])
            reader = csv.reader(file)
            rdata = list(reader)
        except FileNotFoundError:
            sys.exit(1)
            
        header = rdata[0]
        data = rdata[1:]
        print(tabulate(data, header, tablefmt="grid"))
            
def check():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        return True
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()