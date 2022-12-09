import unittest

from day_nine import part_one, part_two


class TestDayNine(unittest.TestCase):
    def test_part_one_example(self):
        self.assertEqual(13, part_one(test=True))

    def test_part_one(self):
        self.assertEqual(5981, part_one())

    def test_part_two_example(self):
        self.assertEqual(36, part_two(test=True))

    def test_part_two(self):
        self.assertEqual(2352, part_two())


if __name__ == '__main__':
    unittest.main()
