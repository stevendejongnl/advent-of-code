import unittest

from day_four import get_sections, intersection, calculate_double_cleaning, contains, calculate_double_cleaning_total


class TestDayThree(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual([2, 3, 4], get_sections('2-4'))
        self.assertEqual([{7}], intersection(([5, 6, 7], [7, 8, 9])))
        self.assertEqual(True, contains([2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7]))
        self.assertEqual(2, calculate_double_cleaning([
            ([2, 3, 4], [6, 7, 8]),
            ([2, 3], [4, 5]),
            ([5, 6, 7], [7, 8, 9]),
            ([2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7]),
            ([6], [4, 5, 6]),
            ([2, 3, 4, 5, 6], [4, 5, 6, 7, 8])
        ]))

    def test_part_two(self):
        self.assertEqual(4, calculate_double_cleaning_total([
            ([2, 3, 4], [6, 7, 8]),
            ([2, 3], [4, 5]),
            ([5, 6, 7], [7, 8, 9]),
            ([2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7]),
            ([6], [4, 5, 6]),
            ([2, 3, 4, 5, 6], [4, 5, 6, 7, 8])
        ]))


if __name__ == '__main__':
    unittest.main()
