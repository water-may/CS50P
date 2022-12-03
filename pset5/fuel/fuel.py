def main():
    while True:
        try:
            fuel = input("Fraction: ")
            if "/" not in fuel:
                continue
            perc = convert(fuel)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(perc))

def convert(fraction):
    x = (fraction.split("/")[0])
    y = (fraction.split("/")[1])
    if not x.isnumeric() or not y.isnumeric():
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
   
    perc = round((int(x)/int(y))*100)
    return perc
    
def gauge(perc):
    if perc <= 1:
        return "E"
    elif  99 <= perc <= 100:
        return "F"
    else:
        return f"{perc}%"
    
if __name__ == "__main__":
    main()
