#!/usr/bin/python3.10
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

anss = ["42", "forty two", "forty-two"]

if ans.lower().strip() in anss:
    print("Yes")
else:
    print("No")