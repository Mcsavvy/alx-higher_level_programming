#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    val = my_list[idx]
    if my_list.index(val) == idx:
        # then it's safe to use remove() because
        # the right item would be removed
        my_list.remove(val)
        return my_list
    copy = my_list.copy()
    my_list.clear()
    for i, val in enumerate(copy):
        if i == idx:
            continue
        my_list.append(val)
    return my_list
