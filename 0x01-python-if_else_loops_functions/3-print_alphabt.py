#!/usr/bin/python3
for c in range(97, 123):
    if(chr(c) != 'q' and chr(c) != 'e'): # if the character is different from q and e
        print("{}".format(chr(c)), end="")
