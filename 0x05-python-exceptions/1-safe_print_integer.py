#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format((intvalue)))
        return True
    except TypeError:
        return False
