#! /usr/bin/python3.10
name = input("File name: ")

mapp = {"gif": "image/gif","jpg": "image/jpeg","jpeg": "image/jpeg","png": "image/png","pdf": "application/pdf","txt": "text/plain","zip": "application/zip"}


ext = name.split(".")[-1].strip(',').strip().lower()

if ext in mapp:
    print(mapp[ext])
else:
    print("application/octet-stream") 