#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_num = 0
    for student, score in a_dictionary.items():
        if score > max_num:
            max_num = score
            max_stud = student
    return max_stud
