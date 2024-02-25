"""Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
None of the arrays will be empty, so you don't have to worry about that!
https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python"""


def remove_every_other(my_list):
    return my_list[::2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
