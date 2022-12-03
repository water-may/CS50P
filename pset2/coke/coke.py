#! /usr/bin/python3.10

init = 50
coins = [5, 10, 25]
while init > 0:
    print(f"Ammount Due: {init}")
    pay = int(input("Insert Coin: "))
    if pay in coins:
        init -= pay
    
    if init <= 0:
        print(f"Change Owed: {-init}")