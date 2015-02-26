"""
Find all permutations of a string
"""

# To be used in the easy answer
import itertools

# Simple solution
def permutations(head, tail=''):
    if len(head) == 0:
        print tail
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])

# Create a generator so we don't use too much memory
def permutations2(word):
    if len(word) <= 1:
        yield word
    else:
        for i in range(len(word)):
            for perm in permutations(word[1:]):
                yield perm[:i] + word[0:1] + perm[i:]

# Using python awesomeness
def permutations3(word):
    return itertools.permutations(word)


# How to use it:
permutations("abc"):

for p in permutations2("abc"):
    print "".join(i)

for p in permutations3("abc"):
    print "".join(i)

