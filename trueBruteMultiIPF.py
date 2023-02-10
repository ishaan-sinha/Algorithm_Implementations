import itertools

def check(rank, attribute_percentages, listOfAttributes):



def bruteForce(attribute):
    listOfAttributes = set(attribute)
    number_of_attributes = len(set(attribute))
    attribute_percentages = {}
    for i in listOfAttributes:
        attribute_percentages[i] = attribute.count(i) / len(attribute)
    possibilities = itertools.permutations(listOfAttributes)
    ipfWorkings = []
    for rank in possibilities:
        works = True
        for i in range(1, len(rank)):
            if(check(rank[:i], attribute_percentages, listOfAttributes) == False):
                works = False
                break
        if(works):
            ipfWorkings.append(rank)
