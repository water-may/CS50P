#! /usr/bin/python3.10

import os
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("notify", help="Enter your notificatin string.")
    args = parser.parse_args()
    # args.print_help
    path = sys.path[0]
    os.system(f"{path}/test_notify.py -h")
    os.system(f"notify-send 'hello world' '{args.notify}'")



    # print(noti)

main()