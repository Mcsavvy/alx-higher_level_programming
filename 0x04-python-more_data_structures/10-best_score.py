#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # get all items in the dict
    items = tuple(a_dictionary.items())

    # set default max
    max_key, max_val = items[0]

    # iterate through the rest of the items
    for key, val in items[1:]:
        # compare this val to the max_val
        if val > max_val:
            # set this val as max_val
            max_key, max_val = key, val
    return max_key
