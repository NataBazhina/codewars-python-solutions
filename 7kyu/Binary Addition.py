"""
Link: https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""

# 1
def add_binary(a,b):
    x = a + b
    binary_num = bin(x)[2:]
    return binary_num

# 2
def add_binary(a,b):
    binary_num = bin(a + b)[2:]
    return binary_num