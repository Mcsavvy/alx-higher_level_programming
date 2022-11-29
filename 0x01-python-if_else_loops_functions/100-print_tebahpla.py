#!/usr/bin/python3
alternate = False
diff = ord('A') - ord('a')
for n in range(ord('z'), ord('a') - 1, -1):
    if alternate:
        n += diff
    alternate = not alternate
    c = chr(n)
    print("{}".format(c), end='')
