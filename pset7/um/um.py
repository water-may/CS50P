#! /usr/bin/python3.10

import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    raw = re.findall(r"\bum(,|\?)?", s, re.IGNORECASE)
    print(raw)
    return len(raw)

if __name__ == "__main__":
    main()
