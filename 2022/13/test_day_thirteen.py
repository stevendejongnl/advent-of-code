import unittest

from day_thirteen import part_one, part_two


class TestDayThirteen(unittest.TestCase):
    def test_part_one_example(self):
        self.assertEqual(13, part_one(test=True))

    def test_part_one(self):
        self.assertEqual(6272, part_one())

    def test_part_two_example(self):
        self.assertEqual(140, part_two(test=True))

    def test_part_two(self):
        self.assertEqual(22288, part_two())


if __name__ == '__main__':
    unittest.main()
