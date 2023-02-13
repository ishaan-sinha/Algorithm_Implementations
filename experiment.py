import itertools
import math

from trueGreedyIPF import createSolution
from trueBruteMultiIPF import bruteForce


root = ["a", "a", "b", "b", "b", "d", "c", "b", "c", "b", "a"]
print(createSolution(root))
print(bruteForce(root))
'''
toCheck = list(itertools.permutations(root))

for i in toCheck:
    i = list(i)
    if createSolution(i) != bruteForce(i):
        print(i)
        break
'''

