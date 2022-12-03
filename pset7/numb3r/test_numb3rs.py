#! /usr/bin/python3.10
import pytest
from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("cat") == False


if __name__ == "__main__":
    main()