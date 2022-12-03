#! /usr/bin/python3.10

import inflect

i = 0
av = []

while True:
    try:
        av.append(input("Name: "))
        i += 1
    except EOFError:
        p = inflect.engine()
        print (f"Adieu, adieu, to {p.join(av)}")
        break
    




