def get_input(test=False):
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file.read().replace('\n\n', '\n').splitlines()


def sunday_morning_parsing_routine(lines):
    monkeys = []
    monkey_dict = {}
    total_monkeys = str(lines).count('Monkey ')
    counter = 0

    for line in lines:
        if 'Monkey ' in line:
            counter = int(line.replace('Monkey ', '').replace(':', ''))
            if counter > 0:
                monkeys.append(monkey_dict)
                monkey_dict = {}

            monkey_dict['monkey'] = counter
            monkey_dict['inspections'] = 0
            monkey_dict['worry'] = 0

        if 'Starting items' in line:
            item_list = [
                int(item)
                for item in line.replace('Starting items: ', '').replace(' ', '').split(',')
            ]
            monkey_dict['items'] = item_list

        if 'Operation' in line:
            operation = line.replace('Operation: new = old ', '').replace(' ', '')
            monkey_dict['operation'] = operation

        if 'Test' in line:
            divide = int(line.replace('Test: divisible by ', ''))
            monkey_dict['divide'] = divide

        if 'If true' in line:
            test_true = int(line.replace('If true: throw to monkey ', '').replace(' ', ''))
            monkey_dict['test_true'] = test_true

        if 'If false' in line:
            test_false = int(line.replace('If false: throw to monkey ', '').replace(' ', ''))
            monkey_dict['test_false'] = test_false

    if counter == total_monkeys - 1:
        monkeys.append(monkey_dict)

    return monkeys


def throw_items(monkeys, monkey, no_divider):
    # sys.set_int_max_str_digits(1_000_000_000)
    bored_divider = 3
    for item in monkey['items'].copy():
        operation = monkey['operation'].replace('old', str(item))
        worried_level = eval(str(item) + operation)

        if no_divider:
            worried_level %= monkey['worry']
        else:
            worried_level //= bored_divider

        divisible = worried_level % monkey['divide'] == 0
        if divisible:
            # print(f"Thrown to monkey {monkey['test_true']} with worried level {worried_level}")
            monkeys[monkey['test_true']]['items'].append(worried_level)
        else:
            # print(f"Thrown to monkey {monkey['test_false']} with worried level {worried_level}")
            monkeys[monkey['test_false']]['items'].append(worried_level)

        monkey['items'].pop(monkey['items'].index(item))
        monkey['inspections'] += 1

    return monkeys


def calculate_worried_levels(monkeys, throws=20):
    no_divider = True if throws > 20 else False

    worry = 1
    for monkey in monkeys:
        worry *= monkey['divide']
    for monkey in monkeys:
        monkey['worry'] = worry

    for _ in range(throws):
        for monkey in monkeys:
            monkeys = throw_items(monkeys, monkey, no_divider)

    active_inspections = [monkey['inspections'] for monkey in monkeys]
    active_inspections.sort(reverse=True)

    return active_inspections[0] * active_inspections[1]


def part_one(test=False):
    file = get_input(test)
    monkeys = sunday_morning_parsing_routine(file)
    total = calculate_worried_levels(monkeys)
    return total


def part_two(test=False):
    file = get_input(test)
    monkeys = sunday_morning_parsing_routine(file)
    total = calculate_worried_levels(monkeys, throws=10_000)
    return total
