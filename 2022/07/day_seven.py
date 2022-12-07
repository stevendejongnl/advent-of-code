def get_input(test=False):
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file.read()


def create_directory_list(lines):
    directories = {'/': {}}
    list_directories = []

    for line in lines:
        cmd = line.split(' ')
        if cmd[0] == '$':
            if cmd[1] == 'ls':
                pass

            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    list_directories.pop()
                elif cmd[2] == '/':
                    list_directories = [directories['/']]
                else:
                    list_directories.append(list_directories[-1][cmd[2]])
        else:
            list_directories[-1][cmd[1]] = {} if cmd[0] == 'dir' else int(cmd[0])

    return directories


def nested_directory_values(directory):
    for value in directory.values():
        if isinstance(value, dict):
            yield from nested_directory_values(value)
        else:
            yield value


def directories_total_size(directories):
    total_sizes = {}

    def search_recursive(start_directories, directory_name=''):
        total = 0
        for directory, sub_directories in start_directories.items():
            if type(sub_directories) != dict:
                total += sub_directories
                continue

            name = directory_name + '/' + directory if directory_name else '/'
            total_sizes[name] = search_recursive(sub_directories, name)
            total += total_sizes[name]
        return total

    search_recursive(directories)

    return total_sizes


def part_one(test=False):
    file = get_input(test)

    lines = file.split('\n')
    directories = create_directory_list(lines)
    total_sizes = directories_total_size(directories)

    return sum(fs for fs in total_sizes.values() if fs <= 100000)


def part_two(test=False):
    file = get_input(test)

    lines = file.split('\n')
    directories = create_directory_list(lines)
    total_sizes = directories_total_size(directories)

    needed_update_space = 70000000 - 30000000

    return min(fs for fs in total_sizes.values() if fs > total_sizes['/'] - needed_update_space)
