def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    dollar = float(d.strip('$'))
    round(dollar, 1)
    return dollar


def percent_to_float(p):
    # TODO
    per = p.strip('%')
    percent = int(per) / 100 
    return percent


main()
