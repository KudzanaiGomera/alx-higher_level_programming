#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_copy = dict(a_dictionary)
    for k in a_dictionary_copy.keys():
        a_dictionary_copy[k] = a_dictionary_copy[k] * 2
    return a_dictionary_copy
