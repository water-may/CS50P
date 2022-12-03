#! /usr/bin/python3.10

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    li = re.search("src=(\"https?://(www\.)?youtube.com/embed/.+\")", s)
    if li:
        raw = li.groups()[0]
        raw = raw.split("/")
        new = f"https://youtu.be/{raw[4]}".split("\"")[0].strip()
        return new

if __name__ == "__main__":
    main()
