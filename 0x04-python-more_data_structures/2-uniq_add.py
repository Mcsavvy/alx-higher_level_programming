#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set from the list to get only unique elements
    unique_list = set(my_list)

    # Initialize a variable to hold the sum
    sum = 0

    # Iterate over the unique elements and add them to the sum
    for item in unique_list:
        sum += item

    # Return the sum
    return sum
