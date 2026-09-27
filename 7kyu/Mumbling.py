"""
Link: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(st):
    new_st = []
    for i, letter in enumerate(st):
        new_st.append(letter.upper() + letter.lower() * i)
    return "-".join(new_st)
