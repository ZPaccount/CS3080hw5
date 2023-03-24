"""
Homework 5-3
Name: Zachary Pace
Date: 3/23/2023
Description: range replacement generator
"""


# Definition for genrange generator
def genrange(stop, start=0, step=1):
    i = start
    while i < stop:
        yield i
        i += step


# For loop to display functionality of genrange
for i in genrange(10, 4, 2):
    print(i)
