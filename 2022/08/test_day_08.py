import unittest


from day_08 import part_one, part_two


class TestDayEight(unittest.TestCase):
    def test_part_one_example(self):
        self.assertEqual(21, part_one(test=True))

    def test_part_one(self):
        result_part_one = part_one()
        print(f'Result of part one: {result_part_one}')
        self.assertTrue(result_part_one < 5830)
        self.assertTrue(result_part_one > 1277)
        self.assertEqual(1708, result_part_one)

    def test_part_two_example(self):
        self.assertEqual(8, part_two(test=True))

    def test_part_two(self):
        result_part_two = part_two()
        print(f'Result of part two: {result_part_two}')
        self.assertEqual(504000, result_part_two)


if __name__ == '__main__':
    unittest.main()
