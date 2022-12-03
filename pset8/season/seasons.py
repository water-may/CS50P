#! /usr/bin/python3
import inflect
import sys
from datetime import date, datetime

p = inflect.engine()

def main():
    print(time(input('Date of Birth: ')))

def time(dat):
    tod = date.today()
    if check(dat):
        dat = datetime.strptime(dat, "%Y-%m-%d").date()
        day = tod-dat
        mi = int(str(day).split()[0]) * 24 * 60
        #print(mi)
        return f'{p.number_to_words(mi, andword="").capitalize()} minutes'

def check(dat):
    try:
        datetime.strptime(dat, "%Y-%m-%d")
        return True
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
