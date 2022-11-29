#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    return print(last_digit, end='') or last_digit
