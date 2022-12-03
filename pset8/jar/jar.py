#! /usr/bin/python3

class Jar:
    def __init__(self, capacity=12):
        if 0 <= capacity:
            self.capacity = capacity
            self.size = 0
        else:
            raise ValueError

    def __str__(self):
        if self._size > 0:
            v = ""
            for _ in range(self._size):
                v += "🍪"
            return v
        elif self._size == 0:
            return f""
        

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if 0 <= capacity :
            self._capacity = capacity
        else:
            raise ValueError

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
