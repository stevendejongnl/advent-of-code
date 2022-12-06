def get_input(test=False):
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file


def list_moves_and_crates(file):
    crates = []
    moves = []
    skipped = False

    for crate in file:
        if crate == '\n':
            skipped = True
            continue
        if not skipped:
            crate = list(crate)
            crate = crate[1::4]
            crates.append(crate)
        else:
            crate = crate.strip()
            if crate[6] != ' ':
                first_num = int(crate[5] + crate[6])
            else:
                first_num = int(crate[5])
            moves.append([first_num, int(crate[-6]), int(crate[-1])])

    return list(reversed(crates)), moves


def crate_to_stack(crates):
    stack = {}
    for index, rows in enumerate(crates):
        if index == 0:
            for values in rows:
                stack[values] = []
        else:
            for sub_index, values in enumerate(rows):
                sub_index = str(sub_index + 1)
                if values != ' ':
                    stack[sub_index].append(values)

    return stack


def rearrange_crates_part_one(crates, moves):
    for move in moves:
        for _ in range(move[0]):
            hold_crate = (crates[str(move[1])][-1])

            crates[str(move[1])].pop()
            crates[str(move[2])].append(hold_crate)

    return crates


def rearrange_crates_part_two(crates, moves):
    for move in moves:
        crate_list = []
        for _ in range(move[0]):
            hold_crate = (crates[str(move[1])][-1])
            crates[str(move[1])].pop()
            crate_list.append(hold_crate)

        for crate in reversed(crate_list):
            crates[str(move[2])].append(crate)

    return crates


def get_order(crates):
    order = []
    for crate in crates.items():
        crate[1].reverse()
        order.append(crate[1][0])
    return ''.join(map(str, order))


def part_one(test=False):
    file = get_input(test)
    crates, moves = list_moves_and_crates(file)
    crates = crate_to_stack(crates)

    crates = rearrange_crates_part_one(crates, moves)

    return get_order(crates)


def part_two(test=False):
    file = get_input(test)
    crates, moves = list_moves_and_crates(file)
    crates = crate_to_stack(crates)

    crates = rearrange_crates_part_two(crates, moves)

    return get_order(crates)
