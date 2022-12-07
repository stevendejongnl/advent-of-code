import unittest

from day_seven import part_one, part_two


class TestDaySeven(unittest.TestCase):
    def test_part_one_example(self):
        self.assertEqual(part_one(test=True), 95437)

    def test_part_one(self):
        result_part_one = part_one()
        print(f'Result of part one: {result_part_one}')
        self.assertIsNotNone(result_part_one)
        self.assertEqual(result_part_one, 1555642)

    def test_part_two_example(self):
        self.assertEqual(part_two(test=True), 24933642)

    def test_part_two(self):
        result_part_two = part_two()
        print(f'Result of part two: {result_part_two}')
        self.assertIsNotNone(result_part_two)
        self.assertEqual(result_part_two, 5974547)


if __name__ == '__main__':
    unittest.main()
