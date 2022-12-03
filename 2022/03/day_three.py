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


def sum_priorities(priorities):
    return sum(priorities)


if __name__ == '__main__':
    input = get_input()
    rucksacks = [
        {
            rucksack.rstrip('\n'): shared_item(split_into_compartments(rucksack.rstrip('\n')))
        }
        for rucksack in input
    ]

    all_priorities = []
    for rucksack in rucksacks:
        for items, priority_item in rucksack.items():

            all_priorities.append(
                priority()['lowercase' if priority_item.islower() else 'uppercase'][priority_item]
            )

    print("Part 1:", sum_priorities(all_priorities))
