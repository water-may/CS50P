#! /usr/bin/python3.10
camel = input("camelCase: ")

for i in range(len(camel)):
    if camel[i].isupper():
        if camel[i-1] == "_":
            continue
        camel = camel[:i]+"_"+camel[i:]

print(f"snake_case: {camel.lower()}")