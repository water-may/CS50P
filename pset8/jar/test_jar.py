#! /usr/bin/python3
import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        _ = Jar(15)
        _ = Jar(-15)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)
    
def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(15)
