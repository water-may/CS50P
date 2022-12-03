#! /usr/bin/python3.10


def main():
    time = input("What time is it? ")
    tt = convert(time)
    if 7.0 <= tt <= 8.0:
        print("breakfast time")
    elif 12.0 <= tt <=13.0:
        print("lunch time")
    elif 18.0 <= tt <= 19.0:
        print("dinner time")


def convert(time):
    return float(time.split(":")[0])+((float(time.split(":")[1]))/60)
    

if __name__ == "__main__":
    main()