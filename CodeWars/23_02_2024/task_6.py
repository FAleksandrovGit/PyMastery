"""Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python"""


def double_char(s):
    return "".join(char * 2 for char in s)


print(double_char("String"))
