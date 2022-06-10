#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = list(a_dictionary.keys())[0]
        for x in a_dictionary.keys():
            if a_dictionary[x] > a_dictionary[max_value]:
                max_value = x
        return max_value
    else:
        return None
