#! /usr/bin/python3.10

from pyfiglet import Figlet 
from sys import exit, argv as av

f = Figlet()

if len(av) != 1:
    if av[1] == "-f" or av[1] == "--font":
     
        fonts = f.getFonts()
        if av[2] in fonts:
            inp = input("Input: ")
            f.setFont(font=av[2])
            print("Output: \n"+f.renderText(inp))
        else:
            exit("Invalid usage")
    else:
        exit("Invalid usage")

elif len(av) == 1:
    inp = input("Input: ")
    print("Output: \n" + f.renderText(inp))