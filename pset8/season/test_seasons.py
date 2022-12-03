#! /usr/bin/python3.10

import pytest
from seasons import check, time

def main():
    test_time()

def test_time():
   assert time("1999-01-01") == 'Twelve million, three hundred thirty-six thousand, four hundred eighty minutes'
   assert time("1998-01-01") == 'Twelve million, eight hundred sixty-two thousand eighty minutes'
   assert time("1995-01-01") == 'Fourteen million, four hundred forty thousand, three hundred twenty minutes'
   

if __name__ == "__main__":
    main()