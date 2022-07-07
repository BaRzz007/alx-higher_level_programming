#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    prev = 0
    if type(roman_string) != str or roman_string == None:
        return result
    roman_numerals = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    for each in roman_string:
        if roman_numerals[each] > prev:
            result = (result - prev) + (roman_numerals[each] - prev)
        else:
            result = result + roman_numerals[each]
        prev = roman_numerals[each]
    return result
