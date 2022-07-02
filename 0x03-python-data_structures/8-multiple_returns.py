#!/usr/bin/python3
def multiple_returns(sentence):
    result_tuple = (0, None)
    if len(sentence) > 0:
        for i, elem in enumerate(sentence):
            if i == 0:
                result_tuple = (len(sentence), elem)
        return result_tuple
    return result_tuple
