#! /usr/bin/python3.10

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #check for length 
    check = False
    if len(s) <= 6:
        #check for first two letters
        fstr = 0
        for i in range(len(s)): 
            if s[i].isalpha():
                fstr += 1
            else:
                fstr = 0
            if fstr >= 2:
                check = True
            
    if not check:
        return False

    #Check for numbers in the middle
    ch = True
    num = ""
    if check:
        for i in range(len(s)):
            if s[i].isnumeric():
                num += s[i]
                for j in s[i:]:
                    if j.isalpha():
                        ch = False
                    
    if len(num) >= 2:
        if num[0] == '0':
            return False

    #Check for periods and space
    if ch:
        for ut in s:
            if not(ut.isalpha() or ut.isnumeric()):
                ch = False

    return ch
            



main()
