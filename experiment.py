import itertools
import math

from trueGreedyIPF import createSolution
from trueBruteMultiIPF import bruteForce
from random import randrange


def kendall_tau_distance(order_a, order_b):
    pairs = itertools.combinations(range(1, len(order_a) + 1), 2)
    distance = 0
    for x, y in pairs:
        a = order_a.index(x) - order_a.index(y)
        b = order_b.index(x) - order_b.index(y)
        if a * b < 0:
            distance += 1
    return distance


from sympy.utilities.iterables import multiset_permutations

root = [ "a", "a", "a", "a", "b", "b", "c", "d"]
rootNum = [i for i in range(1, len(root) + 1)]
toCheck = list(multiset_permutations(root))
'''
a = createSolution(root)
b = bruteForce(root)
print(root)
print(a, kendall_tau_distance(a, rootNum), "greedy")
print(b, kendall_tau_distance(b, rootNum), "brute")
'''
for i in toCheck:
    i = list(i)
    a = createSolution(i)
    b = bruteForce(i)
    if a > b:
        print(i)
        print(a, kendall_tau_distance(a, rootNum))
        print(b, kendall_tau_distance(b, rootNum))
        break
