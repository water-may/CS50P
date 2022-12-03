#! /usr/bin/python3.10

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    #check
    raw = re.search("([0-9]|11|12)(:[0-5][0-9)])? (AM|PM) to ([0-9]|11|12)(:[0-5][0-9])? (AM|PM)", s)
    if raw:
        raw = raw.groups()
        time = []
        if raw[2] == "PM":
            time.append(str(12+int(raw[0])))
            if raw[1]:
                time.append(raw[1])
            else:
                time.append(":00")

            if int(raw[0]) == 12:
                time[0] = "12"
    
        elif raw[2] == "AM":
            time.append(raw[0])
            if raw[1]:
                time.append(raw[1])
            else:
                time.append(":00")
            
            if int(raw[0]) == 12:
                time[0] = "00"
        
        if raw[5] == "PM":
            time.append(str(12+int(raw[3])))
            if raw[4]:
                time.append(raw[4])
            else:
                time.append(":00")

            if int(raw[3]) == 12:
                time[2] = "12"
        elif raw[5] == "AM":
            time.append(raw[3])
            if raw[4]:
                time.append(raw[4])
            else:
                time.append(":00")
            
            if int(raw[3]) == 12:
                time[2] = "00"
    else:
        raise ValueError
    
    if int(time[0]) < 10 and int(time[0]) != 0:
        time[0] = f"0{time[0]}"
    
    if int(time[2]) < 10 and int(time[0]) != 0:
        time[2] = f"0{time[2]}"

    return f"{time[0]}{time[1]} to {time[2]}{time[3]}"

if __name__ == "__main__":
    main()
