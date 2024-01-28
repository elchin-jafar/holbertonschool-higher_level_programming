#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_letter = sentence[0]
    if not sentence:
        first_letter = None
    return (length, first_letter)
