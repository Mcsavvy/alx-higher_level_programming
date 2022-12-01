#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv[1:]
    argc = len(argv)
    word = "argument"
    if argc != 1:
        word += 's'
    print("{} {}{}".format(argc, word, '.' if not argc else ':'))
    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
