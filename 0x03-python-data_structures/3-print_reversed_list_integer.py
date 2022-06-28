#!/usr/bin/python3
def print_reversed_list_integers(my_list):
    my_list.reverse()
    for elem in my_list:
        print("{:d}".format(elem))
