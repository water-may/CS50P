#! /usr/bin/python3.10

def main():
    word = input("Input: ")
    print(shorten(word))
    
def shorten(word):
    vow = ['a', 'e', 'i', 'o', 'u']
    i = 0
    while True:
        if word[i].lower() in vow:
            word = word[:i] + word[i+1:]
            i -= 1
        i += 1
        if i >= len(word):
            break

    return word

if __name__ == "__main__":
    main()