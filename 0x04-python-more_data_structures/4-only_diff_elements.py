#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # can be done like this:
    # set((set_1 - set_2) | (set_2 - set_1))
    #         OR
    # like this:
    # set_1 ^ set_2
    # but i would prefer this:
    return set_1.symmetric_difference(set_2)
