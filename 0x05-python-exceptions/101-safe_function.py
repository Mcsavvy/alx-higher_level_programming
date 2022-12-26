#!/usr/bin/python3

def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except BaseException as exc:
        print("Exception: {}".format(exc), file=stderr)
        return None
