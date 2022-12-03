
def main():
    c = 0
    num = input()
    print(f"{type(num)}  {num}")
    a = int(num.split()[0])
    # try:
    b = int(num.split()[1])
    # except:
    #     if len(num.split()) == 1:
    #         return inter(str(a))

    for i in range(a,b+1):
        if inter(str(i)) == True:
            c += 1
    
    print(c)

def inter(num):
    su = 0
    pro = 1
    for n in num:
        pro *= int(n)
        su += int(n)
    
    if pro % su == 0:
        return True
    else: 
        return False


if __name__ == "__main__":
    main()