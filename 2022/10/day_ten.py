def get_input(test=False):
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file.read().splitlines()


def cycling_two(cycles):
    amounts = [x.split(" ") for x in cycles]
    total = [1]

    for amount in amounts:
        if len(amount) == 2:
            total += [total[-1]] + ([total[-1]+int(amount[-1])])
        else:
            total += [total[-1]]

    return total


def cycling(cycles):
    strengths = []
    cycles_total = 1
    noop = False
    for count, cycle in enumerate(cycles, start=1):
        real_cycles = count * 2
        amount = cycle.replace('addx ', '')
        if amount != 'noop':
            cycles_total += int(amount)

        # if noop:
            # noop = False
        cycle_multiplier = real_cycles == 20 or ((real_cycles - 20) % 40) == 0

        print(cycles_total)
        if cycle_multiplier:
            strengths.append({
                real_cycles: real_cycles * cycles_total
            })
            # cycles_total = 1

    print(strengths)
    strength_list = [[*strength.values()][0] for strength in strengths]
    return sum(strength_list)


def draw_sprite(file, character='#'):
    return "".join(
        [(1 - i % 40) * "\n" +
         (character if abs(i % 40 - cycling_two(file)[i]) <= 1 else ".") for i in range(240)
         ]
    )


def part_one(test=False):
    file = get_input(test)
    return sum([
        *map(lambda x: x * cycling_two(file)[x-1], range(20, 260, 40))
    ])


def part_two(test=False):
    file = get_input(test)
    return draw_sprite(file), draw_sprite(file, character="█")
