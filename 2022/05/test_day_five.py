import unittest

from day_five import part_one, part_two


class TestDayFive(unittest.TestCase):
    def test_part_one_example(self):
        self.assertEqual(
            'CMZ',
            part_one(test=True)
        )

    def test_part_one(self):
        result_part_one = part_one()
        print(f'Result of part one: {result_part_one}')
        self.assertIsNotNone(result_part_one)

    def test_part_two_example(self):
        self.assertEqual(
            'MCD',
            part_two(test=True)
        )

    def test_part_two(self):
        result_part_two = part_two()
        print(f'Result of part two: {result_part_two}')
        self.assertIsNotNone(result_part_two)


if __name__ == '__main__':
    unittest.main()
