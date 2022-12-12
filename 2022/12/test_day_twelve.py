import unittest

import networkx

from day_twelve import get_input, make_grid, get_begin_and_endpoint, calculate_next_to_edges, calculate_total_steps, \
    part_one, part_two


class TestDayTwelve(unittest.TestCase):
    def test_part_one_example(self):
        file = get_input(test=True)
        graph = networkx.DiGraph()

        grid = make_grid(file)
        start, endpoint = get_begin_and_endpoint(grid)
        self.assertEqual([
            (0, 0), (2, 5)
        ], [start, endpoint])

        calculate_next_to_edges(graph, grid)
        self.assertEqual('DiGraph with 40 nodes and 109 edges', str(graph))

        self.assertEqual(31, calculate_total_steps(graph, start, endpoint))

    def test_part_one(self):
        self.assertEqual(408, part_one())

    def test_part_two_example(self):
        self.assertEqual(29, part_two(test=True))

    def test_part_two(self):
        self.assertEqual(399, part_two())


if __name__ == '__main__':
    unittest.main()
