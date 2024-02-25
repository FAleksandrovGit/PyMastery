"Given a random non-negative number, you have to return the digits of this number within an array in reverse order."
"https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python"


def digitize(n):
    return [int(element) for element in reversed(str(n))]


print(digitize(35231))
