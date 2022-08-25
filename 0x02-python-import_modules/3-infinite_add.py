#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print('{:d}'.format(0))
    elif len(argv) == 2:
        print('{:d}'.format(int(argv[1])))
    elif len(argv) > 2:
        sum = 0
        for i in argv[1:]:
            index = argv.index(i)
            sum += int(argv[index])
        print('{:d}'.format(sum))
