#! /usr/bin/python3.10

menu = {
    "baja taco": 4.001,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

tot = 0.00
while True:
    try:
        
        order = input("Item: ")
        tot += menu[order.lower()]
        print(f"Total: ${tot:.2f}")
        
    except EOFError:
        break
    except:
        pass