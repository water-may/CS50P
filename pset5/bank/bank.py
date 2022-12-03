#! /usr/bin/python3.10
def main():
    
    greet = input("Greeting: ")
    print(f"${value(greet)}")

def value(greet):
    if greet.split()[0][0:5].lower() == "hello":
        return 0 
    elif greet.split()[0][0].lower() == "h":
        return 20
    else:
        return 100
    


if __name__ == "__main__":
    main()
