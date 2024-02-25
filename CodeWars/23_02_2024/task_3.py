# Given an array of integers, return a new array with each value doubled.
# https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python

def maps(a):
    return [element * 2 for element in a]


print(maps([1, 2, 3]))