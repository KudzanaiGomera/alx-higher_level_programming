#!/usr/bin/python3
from sys import argv


def main():
    args = len(argv) - 1
    if args == 0:
        print('{} arguments.'.format(args))
    elif args == 1:
        print('1 argument:')
        print('1: {}'.format(argv[args]))
    else:
        print('{} arguments:'.format(args))
        for args in range(1, args + 1):
            print('{}: {}'.format(args, argv[args]))
if __name__ == '__main__':
    main()
