"""
Link: https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python

Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string.

Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.

Examples
'eloquent' --> 'loquen'
'country'  --> 'ountr'
'person'   --> 'erso'
'ab'       --> '' (empty string)
'xyz'      --> 'y'
"""

def remove_char(s):
    return s[1:-1]