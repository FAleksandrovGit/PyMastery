"""Create a function with two arguments that will return an array of the first n multiples of x.
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array or list ( depending on language ).
https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
"""


def count_by(x, n):
    return [element * x for element in range(1, n+1)]


print(count_by(1, 5))
