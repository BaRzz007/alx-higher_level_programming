#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for index in range(x):
            try:
                print("{:d}".format(my_list[index]), end="")
            except (ValueError, TypeError):
                continue
            i += 1
        print()
        return i
    except IndexError:
        raise
