#! /usr/bin/python3.10
import sys
from PIL import Image, ImageOps
def main():
    if check():
        try:
            ims = Image.open("shirt.png")
            imi = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

    
    imi = ImageOps.fit(imi, ims.size)
    imi.paste(ims, ims)
    imi.save(sys.argv[2])
         
def check():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1] != (".png" or ".jpg" or ".jpeg"):
            sys.exit("Input and output have different extensions ")
            print()
        else:
            return True
    except IndexError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()