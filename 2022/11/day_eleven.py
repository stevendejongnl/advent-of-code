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


def calculate_worried_levels(monkeys, throws=20):
    bored_divider = 3
    print(throws)
    inspection = [0 for _ in monkeys]
    for _ in range(throws):
        print("Throws", _)
        for index, monkey in enumerate(monkeys):
            for item in monkey['items'].copy():
                inspection[index] += 1

                sum_string = str(item) + monkey['operation'].replace('old', str(item))
                outcome = 0

                if '*' in sum_string:
                    a, b = sum_string.split('*')
                    outcome = int(int(a) * int(b))
                if '+' in sum_string:
                    a, b = sum_string.split('+')
                    outcome = int(int(a) + int(b))

                worried_level = int(outcome / bored_divider)

                divisible = worried_level / monkey['divide'] == 0
                monkey['items'].pop(monkey['items'].index(item))

                if divisible:
                    # print(f"Thrown to monkey {monkey['test_true']} with worried level {worried_level}")
                    monkeys[monkey['test_true']]['items'].append(worried_level)
                else:
                    # print(f"Thrown to monkey {monkey['test_false']} with worried level {worried_level}")
                    monkeys[monkey['test_false']]['items'].append(worried_level)

        for monkey in monkeys:
            print(f"Monkey {monkey['monkey']}: {monkey['items']}")
        print(" ")

    return monkeys


def part_one(test=False):
    file = get_input(test)
    monkeys = sunday_morning_parsing_routine(file)
    calculate_worried_levels(monkeys)
    return 0


def part_two(test=False):
    file = get_input(test)
    return file
