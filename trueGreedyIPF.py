import itertools
import math

original = [0, 1, 2, 3, 4, 5, 6, 7]
attribute = ["b", "c", "b", "a", "b", "a", "b", "c"]
listOfAttributes = set(attribute)
number_of_attributes = len(set(attribute))
attribute_percentages = {}
for i in listOfAttributes:
    attribute_percentages[i] = attribute.count(i)/len(attribute)

toUse = attribute.copy()
solution = []


def getpossible():
    needed = {}
    for x, y in attribute_percentages.items():
        needed[x] = (len(solution)+1) * attribute_percentages[x]
    for j in listOfAttributes:
        if solution.count(j) < math.floor(needed[j]):
            return [j]
    poss = []
    for j in listOfAttributes:
        if (solution.count(j) + 1) > math.ceil(needed[j]):
            continue
        else:
            poss.append(j)
    return poss


for i in range(1, len(original)+1):
    poss = getpossible()
    res = []
    [res.append(x) for x in toUse if x not in res]
    for j in res:
        if j in poss:
            toUse.remove(j)
            solution.append(j)
            break

