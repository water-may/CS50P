#! /usr/bin/python3.10

import bank as b

def main():
    test_hello()
    test_start_with_h()
    test_other()
    test_insensetive()

def test_hello():
    assert b.value("hello") == 0
    
def test_start_with_h():
    assert b.value("how you doin'") == 20

def test_other():
    assert b.value("dfkaj;dkfja;slfjkw") == 100
    
def test_insensetive():
    assert b.value("K;dkfjaAJKLDJASLslfjkw") == 100
    assert b.value("HOW you Doin'") == 20
    assert b.value("HeLLo") == 0

if __name__ == "__main__":
    main()