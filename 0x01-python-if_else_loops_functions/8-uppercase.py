#!/usr/bin/python3
def uppercase(str):
    for c in str:
        isupper = ord(c) >= ord('a') and ord(c) <= ord('z')
        if isupper:
            # difference between 'a' and 'A'
            diff = ord('A') - ord('a')
            c = chr(ord(c) + diff)
        print("{}".format(c), end='')
    print()
