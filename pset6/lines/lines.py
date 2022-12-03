#! /usr/bin/python3.10

import sys

def main():
    if check():
        print(line())
    
def check():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        return True
    else:
        sys.exit(1)

def line():
    fp = open(sys.argv[1])
    count = 0
    for line in fp:
        if line.lstrip().startswith("#") or len(line.strip()) == 0:
            continue
        else:
            count += 1
    return count 

if __name__ == "__main__":
    main()