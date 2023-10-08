#!/usr/bin/python3
def multiple_returns(sentence):
    fc = 'None'
    if len(sentence) > 0:
        fc = sentence[0]
    return (len(sentence), fc)
