import string


def get_input():
    input_file = 'input.txt'

    file = open(input_file, mode='r')

    return file


def split_into_compartments(rucksack):
    first_compartments = slice(0, len(rucksack) // 2)
    second_compartments = slice(len(rucksack) // 2, len(rucksack))

    return rucksack[first_compartments], rucksack[second_compartments]


def shared_item(rucksack):
    first_compartment, second_compartment = rucksack
    first = [*first_compartment]
    second = [*second_compartment]
    in_both_compartments = ''
    for item in first:
        if item in second:
            in_both_compartments = item

    return in_both_compartments


def group_shared_item(group):
    first = [*group[0]]
    second = [*group[1]]
    third = [*group[2]]

    shared_item_in_group = ''
    for item_first in first:
        for item_second in second:
            if item_first == item_second and item_first in third:
                shared_item_in_group = item_first

    return shared_item_in_group


def priority():
    return {
        "lowercase": {
            char: index + 1
            for index, char in enumerate(string.ascii_lowercase)
        },
        "uppercase": {
            char: index + 27
            for index, char in enumerate(string.ascii_uppercase)
        }
    }


def get_rucksack_groups(rucksacks):
    groups = list(zip(*[iter(rucksacks)]*3))

    return groups


def sum_priorities(priorities):
    return sum(priorities)


def get_rucksacks():
    input = get_input()

    return [
        {
            rucksack.rstrip('\n'): shared_item(split_into_compartments(rucksack.rstrip('\n')))
        }
        for rucksack in input
    ]


def part_one():
    rucksacks = get_rucksacks()

    all_priorities = []
    for rucksack in rucksacks:
        for items, priority_item in rucksack.items():
            all_priorities.append(
                priority()['lowercase' if priority_item.islower() else 'uppercase'][priority_item]
            )

    return sum_priorities(all_priorities)


def part_two():
    rucksacks = get_rucksacks()

    all_priorities = []
    rucksack_list = [
        items
        for rucksack in rucksacks
        for items, _ in rucksack.items()
    ]

    rucksack_groups = get_rucksack_groups(rucksack_list)

    for group in rucksack_groups:
        shared_item_in_group = group_shared_item(group)
        all_priorities.append(
            priority()['lowercase' if shared_item_in_group.islower() else 'uppercase'][shared_item_in_group]
        )

    return sum_priorities(all_priorities)


if __name__ == '__main__':
    print("Part 1:", part_one())
    print("Part 2:", part_two())

