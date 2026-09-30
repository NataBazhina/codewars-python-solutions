"""
Link: https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise,
you can be sure he's not...

Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

Input = ["Peter", "Stephen", "Joe"]
Output = []
Input strings will only contain letters.
Note: keep the original order of the names in the output.
"""
# 1
def friend(x):
    my_friends = []
    for i in x:
        if len(i) == 4:
            my_friends.append(i)
    return my_friends

# 2
def friend(x):
    return [i for i in x if len(i) == 4]
