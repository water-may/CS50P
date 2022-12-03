#! /usr/bin/python3.10
import random
import sys
while True:
    num = input("Level: ")
    if num.isnumeric() and 0 < int(num) <= 100:
        num = int(num)

        #found bug reading discord forum, printed valueError while entering 1 as level and 0 as guess.
        try:
            n = random.randrange(1,num)
        except ValueError:
            n = num

        # takes guess and checks it.
        while True:
            guess = input("Guess: ")
            if guess.isnumeric() and 0 < int(guess) <= 100:
                guess = int(guess)
                if guess > n:
                    print("Too large!")
                elif guess < n:
                    print("Too small!")
                else:
                    print("Just right!")
                    sys.exit()
            else:
                continue
                

    
        
    
        
