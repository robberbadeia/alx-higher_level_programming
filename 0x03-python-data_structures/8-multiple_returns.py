#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) > 0):
        ln = len(sentence)
        first_char = sentence[0]
        return (ln, first_char)
    else:
        ln = len(sentence)
        return(ln, "None")
