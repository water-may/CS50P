#! /usr/bin/python3.10

items = {}

while True:
    try:
        item = input().lower()
        if item in items:
            k = items[item]
            items.pop(item)
            items[item] = k + 1
        else:
            items[item] = 1
    except EOFError:
        break
    except:
        pass

gros = sorted(items)

for gro in gros:
    print(f"{items[gro]} {gro.upper()}")