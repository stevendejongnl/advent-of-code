def get_input(test=False):
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file.read()


def part_one(test=False):
    file = get_input(test)
    return file


def part_two(test=False):
    file = get_input(test)
    return file
