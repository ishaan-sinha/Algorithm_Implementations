import itertools
import math

original = [0, 1, 2, 3, 4, 5, 6, 7]
attribute = ["b", "c", "b", "a", "b", "a", "b", "c"]
listOfAttributes = set(attribute)
number_of_attributes = len(set(attribute))
attribute_percentages = {}
for i in listOfAttributes:
    attribute_percentages[i] = attribute.count(i)/len(attribute)

toUse = ["b", "c", "b", "a", "b", "a", "b", "c"]
solution = []

for i in range(1, (len(original)+1)):
    current = {}
    for x, y in attribute_percentages.items():
        current[x] = y*i
    needed = []
    for j in listOfAttributes:
        if solution.count(j) != math.ceil(current[j]) and solution.count(j) != math.floor(current[j]):
            needed.append(j)
    if len(needed) != 0:
        solution.append(needed[0])
        toUse.remove(needed[0])
    else:
        for k in set(toUse):
            position = toUse.index(k)
            if math.ceil((len(solution) + 1) * attribute_percentages[k]) >= solution.count(k) + 1:
                toUse.pop(position)
                solution.append(k)
                break
            else:
                continue
print(solution)
