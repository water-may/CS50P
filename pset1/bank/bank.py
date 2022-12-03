#! /usr/bin/python3.10
greet = input("Greeting: ")

if greet.split()[0][0:5].lower() == "hello":
    print("$0") 
elif greet.split()[0][0].lower() == "h":
    print("$20")
else:
    print("$100")