#! /usr/bin/python3
import sys
import csv


def main():
    if check():
        try:
            file = open(sys.argv[1])
            reader = csv.reader(file)
            rdata = list(reader)
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

    ofile = open(sys.argv[2], "w")
    ofile.write("first,last,house\n")
    lname=[]
    for line in rdata[1:]:
    
        lname = line[0].split(",")[0]
        fname = line[0].split()[-1].strip()
        house = line[1].strip()
        ofile.write(f'{fname},{lname},{house}\n')


def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return True

if __name__ == "__main__":
    main()