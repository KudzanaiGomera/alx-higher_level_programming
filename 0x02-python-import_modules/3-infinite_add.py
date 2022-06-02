#!/usr/bin/python3
import sys


def main():
    ar = sys.argv
    ar = ar[1:]
    sum = 0
    for i in ar:
        sum += int(i)
    print('{}'.format(sum))
if __name__ == '__main__':
    main()
