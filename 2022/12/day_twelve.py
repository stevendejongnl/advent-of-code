import networkx  # 🫣


def get_input(test=False) -> list:
    input_file = f"input{'_test' if test else ''}.txt"

    file = open(input_file, mode='r')

    return file.read().splitlines()


def make_grid(path) -> dict[tuple[int, int], str]:
    return {
        (latitude, longitude): character
        for latitude, row in enumerate(path)
        for longitude, character in enumerate(row)
    }


def get_begin_and_endpoint(grid) -> tuple[tuple[int, int], tuple[int, int]]:
    ini_the_beninging = [key for key in grid.keys() if grid[key] == "S"][0]
    endpoint = [key for key in grid.keys() if grid[key] == "E"][0]

    grid[ini_the_beninging] = "s"
    grid[endpoint] = "z"

    return ini_the_beninging, endpoint


def calculate_next_to_edges(graph, grid) -> None:
    for latitude, longitude in grid.keys():
        next_to: list[tuple[int, int]] = [
            (latitude + 1, longitude),
            (latitude - 1, longitude),
            (latitude, longitude + 1),
            (latitude, longitude - 1)
        ]
        next_to = [point for point in next_to if point in grid.keys()]
        next_to = [
            point for point in next_to
            if (ord(grid[point]) - ord(grid[(latitude, longitude)])) <= 1
        ]

        for points in next_to:
            graph.add_edge((latitude, longitude), points)


def calculate_total_steps(graph, start, endpoint) -> int:
    shortest_path = networkx.shortest_path(graph, start, endpoint)
    total_steps = len(shortest_path) - 1

    return total_steps


def min_path(graph, grid, endpoint) -> int:
    candidates = [key for key in grid.keys() if grid[key] == "a"]
    paths = [
        calculate_total_steps(graph, candidate, endpoint)
        for candidate in candidates
        if networkx.has_path(graph, candidate, endpoint)
    ]

    return min(paths)


def part_one() -> int:
    file = get_input(test=False)
    graph = networkx.DiGraph()

    grid = make_grid(file)
    start, endpoint = get_begin_and_endpoint(grid)
    calculate_next_to_edges(graph, grid)

    total_steps = calculate_total_steps(graph, start, endpoint)

    return total_steps


def part_two(test=False) -> int:
    file = get_input(test)
    graph = networkx.DiGraph()

    grid = make_grid(file)
    begin, endpoint = get_begin_and_endpoint(grid)
    calculate_next_to_edges(graph, grid)

    steps = min_path(graph, grid, endpoint)

    return steps
