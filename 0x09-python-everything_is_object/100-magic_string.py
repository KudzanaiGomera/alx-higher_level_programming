#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "c", getattr(magic_string, "c", -1) + 1)
    return "Holberton" + ", Holberton" * magic_string.c
