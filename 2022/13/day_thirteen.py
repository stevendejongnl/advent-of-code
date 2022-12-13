def get_input(test=False):
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file.read().replace('\n\n', '\n').splitlines()


def append_packet_number(packet: str, index: int, parsed: list) -> int:
    end = index
    while end < len(packet) and packet[end].isnumeric():
        end += 1

    parsed.append(int(packet[index:end]))

    return end


def parse_packet(packet: str, index: int = 1) -> tuple[int, list]:
    parsed = []

    index += 1

    while index < len(packet):
        if packet[index] == '[':
            index, sub_parsed = parse_packet(packet, index)
            parsed.append(sub_parsed)
            continue

        if packet[index].isnumeric():
            index = append_packet_number(packet, index, parsed)

        if packet[index] == ',':
            index += 1
            continue

        if packet[index] == ']':
            break

    return index + 1, parsed


def split_into_pairs(packets: list[str]) -> list[list]:
    pairs = [
        parse_packet(packet, 0)[1]
        for packet in packets
    ]

    return pairs


def move_when_list(left: list | int, right: list | int):
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    return compare_small_with_big_list(left, right)


def compare_small_with_big_list(small: list, big: list) -> int:
    for left, right in zip(small, big):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            elif left > right:
                return 1
            continue

        if isinstance(left, list) or isinstance(right, list):
            inner_list = move_when_list(left, right)

            if not inner_list:
                continue

            return inner_list

    if len(small) < len(big):
        return -1
    elif len(small) > len(big):
        return 1
    else:
        return 0


def total_indices_of_pairs(pairs: list[list]) -> int:
    result = 0
    small_list = pairs[:-1:2]
    big_list = pairs[1::2]

    for index, (small, big) in enumerate(zip(small_list, big_list)):
        compare = compare_small_with_big_list(list(small), list(big))
        if compare == -1:
            result += index + 1

    return result


def part_one(test=False) -> int:
    packets = get_input(test)

    pairs = split_into_pairs(packets)
    result = total_indices_of_pairs(pairs)

    return result


def part_two(test=False):
    pass
