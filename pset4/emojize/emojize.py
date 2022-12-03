#! /usr/bin/python3

import emoji

code = input("Input: ")

try:
    print(f'Output: {emoji.emojize(code, language="alias")}')
except:
    pass
