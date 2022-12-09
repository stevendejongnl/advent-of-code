from enum import Enum


def get_input(test=False, two=False):
    input_file = f"input{'_test' if test else ''}{'_part_two' if two else ''}.txt"

    file = open(input_file, mode='r')

    return file.read()


class Direction(Enum):
    right = 'R'
    left = 'L'
    up = 'U'
    down = 'D'


def parse_lines(file):
    new_lines = []
    lines = file.splitlines()
    for line in lines:
        new_lines.append(line.rstrip('\n').split(' '))

    return new_lines


def knot_positions(coordinates, moves):
    position = coordinates
    path = [coordinates]
    for move in moves:
        steps = set_move(position, move)
        path = path + steps
        position = steps[-1]

    return path


def get_position(coordinate_x, coordinate_y, subtract=False, change_y=False):
    new_x = coordinate_x
    new_y = coordinate_y
    if not subtract and not change_y:
        new_x = coordinate_x + 1

    if subtract and not change_y:
        new_x = coordinate_x - 1

    if not subtract and change_y:
        new_y = coordinate_y + 1

    if subtract and change_y:
        new_y = coordinate_y - 1

    return [new_x, new_y]


def set_move(position, move):
    steps = []
    distance = int(move[1])

    if 0 == distance:
        steps.append(position)
        return steps

    if move[0] == Direction.right.value:
        for _ in range(distance):
            position = get_position(position[0], position[1])
            steps.append(position)

    if move[0] == Direction.left.value:
        for _ in range(distance):
            position = get_position(position[0], position[1], subtract=True)
            steps.append(position)

    if move[0] == Direction.up.value:
        for _ in range(distance):
            position = get_position(position[0], position[1], change_y=True)
            steps.append(position)

    if move[0] == Direction.down.value:
        for _ in range(distance):
            position = get_position(position[0], position[1], subtract=True, change_y=True)
            steps.append(position)

    return steps


def create_path(coordinates, path):
    coordinate = coordinates
    max_distance = 1
    list_path = [coordinate]

    for position in path:
        horizontal_distance = position[0] - coordinate[0]
        vertical_distance = position[1] - coordinate[1]
        horizontal_travel = 0
        vertical_travel = 0

        if abs(vertical_distance) <= max_distance and abs(horizontal_distance) <= max_distance:
            list_path.append(coordinate)
            continue

        if abs(vertical_distance):
            vertical_travel = 1

        if abs(horizontal_distance):
            horizontal_travel = 1

        if vertical_distance < 0:
            vertical_travel *= -1

        if horizontal_distance < 0:
            horizontal_travel *= -1

        coordinate = [coordinate[0] + horizontal_travel, coordinate[1] + vertical_travel]
        list_path.append(coordinate)
    return list_path


def total_positions(path):
    positions = len(set([
        f"{p[0]}-{p[1]}"
        for p in path
    ]))

    return positions


def part_one(test=False):
    file = get_input(test)
    lines = parse_lines(file)

    coordinates = [0, 0]
    path = knot_positions(coordinates, lines)
    list_path = create_path(coordinates, path)
    positions = total_positions(list_path)

    return positions


def part_two(test=False):
    if test:
        file = get_input(test, two=True)
    else:
        file = get_input()
    lines = parse_lines(file)

    coordinates = [0, 0]
    path = knot_positions(coordinates, lines)
    list_path = [path]
    for i in range(9):
        list_path.append(create_path(coordinates, list_path[i]))
    positions = total_positions(list_path[-1])

    return positions
