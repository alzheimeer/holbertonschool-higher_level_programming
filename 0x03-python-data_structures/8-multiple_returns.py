#!/usr/bin/python3
def multiple_returns(sentence):
    lenx = len(sentence)
    if (lenx == 0):
        L = None
    else:
        L = sentence[0]
    t = (lenx, L)
    return(t)
