import math

initial_rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#a = 1, b = 2, c = 3, d = 4, e = 5
attributes = [1, 1, 2, 2, 2, 4, 3, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
number_of_attributes = len(set(attributes))
attribute_percentages = [attributes.count(i)/len(attributes) for i in range(1, number_of_attributes+1)]


def bot(rank):
    i = attributes[0:rank].count(attributes[rank])
    return math.floor((i-1)/attribute_percentages[attributes[rank] - 1]) + 1


def top(rank):
    i = attributes[0:rank].count(attributes[rank])
    return math.ceil(i/(attribute_percentages[attributes[rank] - 1]))


top_list = [top(i) for i in range(0, len(initial_rank))]
bot_list = [bot(i) for i in range(0, len(initial_rank))]

print(top_list)
print(bot_list)