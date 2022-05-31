#!/usr/bin/python3
def remove_char_at(str, n):
    empty = ""
    for x, y in enumerate(str):
        if x != n:
            empty += y
    return empty
