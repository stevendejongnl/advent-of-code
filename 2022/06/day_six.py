def get_input(test=False):
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file.read()


def unique(characters) -> bool:
    seen = set()
    return not any(character in seen or seen.add(character) for character in characters)


def find_marker(stream, total_different=4):
    for index, character in enumerate(stream):
        marker = stream[index:index+total_different]

        unique_characters = unique(marker)
        complete_after_characters = index + total_different
        if unique_characters is True:
            return marker, complete_after_characters


def part_one(test=False):
    file = get_input(test)
    return find_marker(file)


def part_two(test=False):
    file = get_input(test)
    return find_marker(file, total_different=14)
