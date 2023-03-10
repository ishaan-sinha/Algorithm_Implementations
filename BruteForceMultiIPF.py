import itertools
import math


def kendall_tau_distance(order_a, order_b):
    pairs = itertools.combinations(range(0, len(order_a)), 2)
    distance = 0
    for x, y in pairs:
        a = order_a.index(x) - order_a.index(y)
        b = order_b.index(x) - order_b.index(y)
        if a * b < 0:
            distance += 1
    return distance



def bruteForce(attribute):
    original = [i for i in range(len(attribute))]
    listOfAttributes = set(attribute)
    number_of_attributes = len(set(attribute))
    attribute_percentages = {}
    for i in listOfAttributes:
        attribute_percentages[i] = attribute.count(i) / len(attribute)

    possibilities = itertools.permutations(original)
    ipfWorkings = []

    for order in possibilities:
        flag = True
        for k in range(len(order)):
            sub = order[0:k + 1]
            soFar = [attribute[i] for i in sub]
            for i in listOfAttributes:
                if (soFar.count(i) == math.floor(attribute_percentages[i] * len(sub)) or soFar.count(i) == math.ceil(
                        attribute_percentages[i] * len(sub))):
                    continue
                else:
                    flag = False
        if (flag == True):
            ipfWorkings.append(order)
    solution = []
    lowestDistance = 10000
    for order in ipfWorkings:
        if kendall_tau_distance(original, order) < lowestDistance:
            lowestDistance = kendall_tau_distance(original, order)
            solution = order
    return [i + 1 for i in solution]
