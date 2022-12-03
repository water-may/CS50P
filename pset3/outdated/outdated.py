#! /usr/bin/python3.10
mth = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def check(y, m, d):
    if int(m) <= 0 or int(m) > 12:
        return False
    elif int(d) <= 0 or int(d) > 30:
        return False
    
    return True

while True:
    date = (input("Date: ")).strip()

    try:
        x,y,z = date.split("/")
        if not x.isnumeric():
            continue
        if not check(z, x, y):
            continue
        print(f"{z}-{x.zfill(2)}-{y.zfill(2)}")
        break
    except:
        x = date.split(" ")
        y = x[1].split(",")
        x[1] = y[0]
        if x[0].capitalize() in mth:
            x[0] = mth.index(x[0].capitalize()) + 1
            if not check(x[2], str(x[0]), x[1]):
                continue
            elif ',' not in date:
                continue
            else:
                print(f"{x[2]}-{str(x[0]).zfill(2)}-{x[1].zfill(2)}")
                break
        else:
            pass    
    else:
        pass


