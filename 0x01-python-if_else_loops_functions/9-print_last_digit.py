#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    if number < 0:
        return last - 10
    return last
