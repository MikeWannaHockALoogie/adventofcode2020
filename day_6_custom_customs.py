from functools import reduce

file = 'day_6_custom_customs_input.txt'
groups = open(file).read().split('\n\n')

s1 = sum(len(set(group.replace('\n',''))) for group in groups)
print(s1)

s2= sum([len(reduce(set.intersection, [set(person) for person in group.split('\n')])) for group in groups])
print(s2)