#! /usr/bin/python3.10

while True:
    fuel = input("Fraction: ")
    try:
        x = int(fuel.split("/")[0])
        y = int(fuel.split("/")[1])
        perc = round((x/y)*100)
        if perc <= 1:
            print("E")
        elif  99 <= perc <= 100:
            print("F")
        elif perc <= 0 or perc >= 100:
            continue
        else:
            print(f"{perc}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
    
    


