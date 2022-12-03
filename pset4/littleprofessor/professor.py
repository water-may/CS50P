#! /usr/bin/python3.10
import random
import sys

def main():
    score = 0
    level = get_level()

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        c = x + y
        for j in range(3):
            ans = input(f"{x} + {y} = ")
            if ans.isnumeric() and int(ans) == c:
                score += 1
                break
            else:
                print("EEE")
                if j == 2:
                    print(f"{x} + {y} = {c}")
                    break
        
    print(f"Score: {score}")
    sys.exit()


def get_level():
    while True:
        try:
            level = int(input("Level: ")) 
            if 1 <= level <= 3: 
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
