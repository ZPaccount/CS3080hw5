"""
Homework 5-2
Name: Zachary Pace
Date: 3/23/2023
Description: Pythagorean triplet generator
"""


# Definition for pyt generator
def pyt(n):
    z = 1
    i = 0
    # Search for n nuber of values to generate
    while i < n:
        z += 1
        # for each z value use a nested for loop to see if it's pythagorean
        for y in range(z):
            for x in range(y):
                if x**2 + y**2 == z**2:
                    yield [x, y, z]
                    i += 1


# Definition for take function
def take(n, Pyt):
    gen = Pyt(n) # passing a pointer to the generator
    OutputList = [] # not sure why this is needed, but it very much is
    for i in range(n):
        OutputList.append(next(gen))
    return OutputList


print(take(10, pyt))
