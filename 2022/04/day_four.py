import math


def get_input():
    input_file = 'input.txt'

    file = open(input_file, mode='r')

    return file


def get_sections(sections: str):
    first_section, last_section = sections.split('-')
    section_range = range(math.ceil(int(first_section)), math.floor(int(last_section)) + 1)
    section_list: list = [
        x
        for x in section_range
    ]

    return section_list


def intersection(sections):
    return [set(sections[0]) & set(sections[1])]


def contains(first_sections, second_sections):
    return set(first_sections).issubset(second_sections) or set(second_sections).issubset(first_sections)


def calculate_double_cleaning(sections_by_pair: list[tuple]):
    double_cleaning = 0
    for pair in sections_by_pair:
        first_elf = pair[0]
        second_elf = pair[1]

        if contains(first_elf, second_elf):
            double_cleaning += 1

    return double_cleaning


def calculate_double_cleaning_total(sections: list):
    double_cleaning = 0
    for section in sections:
        if len(intersection(section)[0]) != 0:
            double_cleaning += 1

    return double_cleaning


def part_one():
    sections = [
        (
            get_sections(pair.rstrip('\n').split(',')[0]),
            get_sections(pair.rstrip('\n').split(',')[1])
        )
        for pair in get_input()
    ]

    return calculate_double_cleaning(sections)


def part_two():
    sections = [
        (
            get_sections(pair.rstrip('\n').split(',')[0]),
            get_sections(pair.rstrip('\n').split(',')[1])
        )
        for pair in get_input()
    ]

    return calculate_double_cleaning_total(sections)


if __name__ == '__main__':
    print("Part 1:", part_one())
    print("Part 2:", part_two())
