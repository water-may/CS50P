#! /usr/bin/python3.10

word = input("Input: ")

vow = ['a', 'e', 'i', 'o', 'u']

i = 0
while True:
   
    if word[i].lower() in vow:
        word = word[:i] + word[i+1:]
        i -= 1
    i += 1
    if i >= len(word):
        break

print(word)