# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
# https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/python

def greet(name, owner):
    return "".join("Hello boss" if name == owner else "Hello guest")


greet('Daniel', 'Daniel')