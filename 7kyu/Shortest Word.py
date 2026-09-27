"""
Link: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

# 1
def find_short(s):
    st = s.split()
    lengths = [len(i) for i in st]
    return min(lengths)


# 2
def find_short(s):
    st = s.split()
    return min([len(i) for i in st])

# 3
def find_short(s):
    return min(len(i) for i in s.split())