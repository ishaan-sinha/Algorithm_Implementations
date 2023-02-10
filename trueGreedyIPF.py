import itertools
import math





def getpossible(solution, attribute_percentages, listOfAttributes):
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


def createSolution(attribute):
    solution = []
    toUse = attribute.copy()
    listOfAttributes = set(attribute)
    number_of_attributes = len(set(attribute))
    attribute_percentages = {}
    for i in listOfAttributes:
        attribute_percentages[i] = attribute.count(i) / len(attribute)

    for i in range(1, len(attribute)+1):
        poss = getpossible(solution, attribute_percentages, listOfAttributes)
        res = []
        [res.append(x) for x in toUse if x not in res]
        for j in res:
            if j in poss:
                toUse.remove(j)
                solution.append(j)
                break
    return solution

print(createSolution(["a", "b", "a", "c", "c", "b", "b", "a", "c"]))
