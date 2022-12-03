#! /usr/bin/python3.10
import sys
import plates as p

def main():
    # test_fst_letter()
    # test_midnum()
    # test_len()
    # test_symbol()
    test_oth()

def test_oth():
    assert p.is_valid("CS05") == False
    assert p.is_valid("CS50P2") == False
    assert p.is_valid("PI3.14") == False
    assert p.is_valid("H") == False
    assert p.is_valid("OUTATIME") == False
    assert p.is_valid("CS50") == True
    assert p.is_valid("ECTO88") == True
    assert p.is_valid("NRVOUS") == True
    assert p.is_valid("7777") == False

# def test_fst_letter():
#     assert p.is_valid("77daf") == False

# def test_len():
#     assert p.is_valid("CS55") == True
#     assert p.is_valid("he00000") == False
#     assert p.is_valid("h") == False
    
# def test_midnum():
#     assert p.is_valid("he000A") == False

# def test_symbol():
#     assert p.is_valid("he%$./") == False
    


if __name__ == "__main__":
    main()