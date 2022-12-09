def get_input(test=False):
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file.read().splitlines()


def get_total_visible(row, tree_row, column, tree_column, middle_tree):
    return (
        all(tree < middle_tree for tree in row[:tree_row])
        or all(tree < middle_tree for tree in row[tree_row + 1:])
        or all(tree < middle_tree for tree in column[:tree_column])
        or all(tree < middle_tree for tree in column[tree_column + 1:])
    )


def get_highest(highest, row, tree_row, column, tree_column, middle_tree, vertical, horizontal):
    from_left = next(
        (tree for tree in range(1, tree_row) if row[tree_row - tree] >= middle_tree),
        tree_row
    )
    from_right = next(
        (tree for tree in range(1, vertical - tree_row) if row[tree_row + tree] >= middle_tree),
        vertical - tree_row - 1
    )
    from_up = next(
        (tree for tree in range(1, tree_column) if column[tree_column - tree] >= middle_tree),
        tree_column
    )
    from_down = next(
        (tree for tree in range(1, horizontal - tree_column) if column[tree_column + tree] >= middle_tree),
        horizontal - tree_column - 1
    )

    return max(highest, from_left * from_right * from_up * from_down)


def calculator_thing(trees, get_by_highest=False):
    tree_list = [[int(tree) for tree in row.strip()] for row in trees]
    horizontal, vertical = len(tree_list), len(tree_list[0])

    highest = 0
    counter = 0
    for tree_row in range(vertical):
        column = [tree_list[tree_column][tree_row] for tree_column in range(horizontal)]
        for tree_column in range(horizontal):
            row = tree_list[tree_column]
            middle_tree = tree_list[tree_column][tree_row]

            if not get_by_highest:
                counter += get_total_visible(row, tree_row, column, tree_column, middle_tree)

            if get_by_highest:
                highest = get_highest(highest, row, tree_row, column, tree_column, middle_tree, vertical, horizontal)

    if get_by_highest:
        return highest
    return counter


def part_one(test=False):
    file = get_input(test)

    return calculator_thing(file)


def part_two(test=False):
    file = get_input(test)

    return calculator_thing(file, get_by_highest=True)
