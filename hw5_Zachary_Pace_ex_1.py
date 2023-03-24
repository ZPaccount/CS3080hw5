"""
Homework 5-1
Name: Zachary Pace
Date: 3/23/2023
Description: make an iterator that iterates backwards
"""


# define ReverseIter Iterator
class ReverseIter:
    def __init__(self, n):
        self.i = 1
        self.List = n

    # define __next__ function
    def __next__(self):
        if self.i < len(self.List) + 1:
            result = self.List[-self.i]
            self.i += 1
            return result
        else:
            raise StopIteration()


# Code for testing ReverseIter
test = [1, 2, 3, 4, 5]
it = ReverseIter(test)
for i in range(len(test)):
    print(str(next(it)))
