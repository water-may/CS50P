#! /usr/bin/python3.10

import pytest
from response import validate

def main():
    test_validate()

def test_validate():
   assert validate("um") == "Invalid"
   

if __name__ == "__main__":
    main()