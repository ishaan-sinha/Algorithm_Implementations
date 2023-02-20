import itertools
import math
from sympy.utilities.iterables import multiset_permutations


def kendall_tau_distance(order_a, order_b):
    pairs = itertools.combinations(range(1, len(order_a)+1), 2)
    distance = 0
    for x, y in pairs:
        a = order_a.index(x) - order_a.index(y)
        b = order_b.index(x) - order_b.index(y)
        if a * b < 0:
            distance += 1
    return distance

def check(rank, attribute_percentages, listOfAttributes):
    for i in listOfAttributes:
        if rank.count(i) != math.floor(attribute_percentages[i] * len(rank)) and rank.count(i) != math.ceil(attribute_percentages[i] * len(rank)):
            return False
    return True


def bruteForce(attribute):
    listOfAttributes = set(attribute)
    number_of_attributes = len(set(attribute))
    attribute_percentages = {}
    indicesOfAttributes = {}
    for i in listOfAttributes:
        attribute_percentages[i] = attribute.count(i) / len(attribute)
        indicesOfAttributes[i] = [j for j in range(len(attribute)) if attribute[j] == i]
    possibilities = multiset_permutations(attribute)
    ipfWorkings = []
    for rank in possibilities:
        works = True
        for i in range(1, len(rank)):
            if(check(rank[:i], attribute_percentages, listOfAttributes) == False):
                works = False
                break
        if(works):
            ipfWorkings.append(rank)
    solution = []
    solutionAtt = []
    lowestDistance = 10000
    for rank in ipfWorkings:
        indices = indicesOfAttributes.copy()
        solNum = []
        for i in rank:
            solNum.append(indices[i][0] + 1)
            indices[i] = indices[i][1:]
        if kendall_tau_distance(solNum, [k for k in range(1, len(attribute)+1)]) < lowestDistance:
            solution = solNum
            solutionAtt = rank
            lowestDistance = kendall_tau_distance(solNum, [i for i in range(1, len(attribute)+1)])
    return list(solution)

