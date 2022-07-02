#!/usr/bin/python3
def multiple_returns(sentence):
    result_tuple = (None, 0)
    if len(sentence) > 0:
        for i, elem in enumerate(sentence):
            if i == 0:
                result_tuple = (elem, len(sentence))
        return result_tuple
    return result_tuple
