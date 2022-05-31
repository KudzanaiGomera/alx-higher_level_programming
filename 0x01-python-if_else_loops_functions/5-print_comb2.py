#!/usr/bin/python3
for x in range(0, 100):
    if x < 99:
        print('{0:02d}'.format(int(x)), end=", ")
    else:
        print('{}'.format(int(x)))
