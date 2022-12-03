#! /usr/bin/python3.10

import twttr as t

def main():
    test_twttr()

def test_twttr():
    assert t.shorten("Twitter") == "Twttr"
    assert t.shorten("What's your name?") == "Wht's yr nm?"
    assert t.shorten("CS50") == "CS50"
    assert t.shorten("PYTHON") == "PYTHN"

if __name__ == "__main__":
    main()