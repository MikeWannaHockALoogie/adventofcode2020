import re
from copy import deepcopy


class Bag():

    def __init__(self, name: str, contents: dict):
        self.name = name
        self.contents = contents
        self.count = 0

    def __repr__(self):
        return f'{self.name} has {self.contents}'

    def contains(self, color):
        for bag in self.contents.keys():
            if re.search(color, bag):
                return True
        return False

    def count_bags(self):
        return sum(self.contents.values())


def parse(f):
    data = open(f).readlines()

    for bag in data:
        bag = [i.strip() for i in bag.split('contain')]
        bag_name = bag[0].replace(' bags', '').replace(
            ' bag', '').rstrip('')
        content_counts = [int(i.strip()) for i in re.findall(
            '[\d+]\s', bag[1])]

        contents = re.findall(
            '([a-z\s]+)', bag[1].strip().replace('bags', '').replace('bag', ''))
        if len(content_counts) != len(contents):

            for i in contents:
                if i == ' ':
                    contents.remove(i)
                if i == 'no other ':
                    contents.remove(i)

        bag_contents = list(zip(content_counts, contents))

        b = Bag(name=bag_name, contents={
            content[1].strip(): content[0] for content in bag_contents})

        bags.append(b)


starting_bag = Bag(name='shiny gold', contents=[])


test_file = 'test_input.txt'
file = 'day_7_handy_haversacks_input.txt'
bags = []
parse(
    file)
bags_to_find = [starting_bag]
bags_found = []
count = 0

while True:
    if bags_to_find == []:
        break
    current_bag = bags_to_find.pop().name.strip()
    # print(f'searching for {current_bag}')
    for bag in bags:
        if bag.contains(current_bag):
            count += 1
            # print(bag)
            bags_to_find.append(bag)
            bags_found.append(bag)


b = set([bag.name for bag in bags_found])
print(len(b))
shiny_gold = [bag for bag in bags if bag.name == 'shiny gold'][0]
bags_to_count = [shiny_gold]
count = 0
while bags_to_count:
    current_bag = bags_to_count.pop(0)
    count += current_bag.count_bags()
    for key, value in current_bag.contents.items():
        b = [bag for bag in bags if bag.name == key][0]
        for i in range(value):
            bags_to_count.append(b)


print(count)
