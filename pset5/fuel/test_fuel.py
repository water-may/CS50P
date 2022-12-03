#! /usr/bin/python3.10
import pytest
import fuel as f

def main():

    test_oth()

def test_oth():
    assert f.convert("3/4") == 75
    assert f.convert("1/3") == 33
    assert f.convert("2/3") == 67
    assert f.gauge(f.convert("0/100")) == "E"
    assert f.gauge(f.convert("1/100")) == "E"
    assert f.gauge(f.convert("100/100")) == "F"
    assert f.gauge(f.convert("99/100")) == "F"
    assert f.gauge(50) == "50%" 
    
    
    

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        f.convert("100/0")

def test_valuerror():
    with pytest.raises(ValueError):
        f.convert("three/four")
        f.convert("1.5/4")
        f.convert("3/5.5")
        f.convert("10/3")
        

if __name__ == "__main__":
    main()