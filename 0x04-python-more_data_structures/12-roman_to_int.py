#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    numerals = (
            ('MMM', 3000), ('MM', 2000), ('M', 1000), ('CM', 900),
            ('DCCC', 800), ('DCC', 700), ('DC', 600), ('D', 500),
            ('CD', 400), ('CCC', 300), ('CC', 200), ('C', 100),
            ('XC', 90), ('LXXX', 80), ('LXX', 70), ('LX', 60),
            ('L', 50), ('XL', 40), ('XXX', 30), ('XX', 20),
            ('X', 10), ('IX', 9), ('VIII', 8), ('VII', 7),
            ('VI', 6), ('V', 5), ('IV', 4), ('III', 3),
            ('II', 2), ('I', 1))
    total = 0
    while roman_string:
        for symbol, value in numerals:
            if roman_string.startswith(symbol):
                total += value
                roman_string = roman_string[len(symbol):]
    return total
