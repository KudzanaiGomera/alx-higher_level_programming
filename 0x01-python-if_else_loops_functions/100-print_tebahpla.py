#!/usr/bin/python3
for alpha in range(122, 96, -1):
    if alpha % 2 == 1:
        alpha = alpha - 32
    print('{:s}'.format(chr(alpha)), end='')
