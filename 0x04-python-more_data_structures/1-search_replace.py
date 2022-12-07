#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list with the same size as the input list
    replaced_list = [0 for i in range(len(my_list))]

    # Iterate over the elements of the input list and replace
    # each occurrence of the search element with the replace element.
    for i in range(len(my_list)):
        if my_list[i] == search:
            replaced_list[i] = replace
        else:
            replaced_list[i] = my_list[i]

    # Return the new list
    return replaced_list
