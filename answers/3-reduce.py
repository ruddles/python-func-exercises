from functools import reduce

# Write a reduce function that finds the longest word
words = ["functional", "is", "the", "best"]


def return_longest(a, b):
    if len(a) > len(b):
        return a
    else:
        return b


longest = reduce(return_longest, words)
print(longest)  # expected functional
