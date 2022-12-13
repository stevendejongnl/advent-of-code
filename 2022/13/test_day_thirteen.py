import unittest

from day_thirteen import part_one


class TestDayThirteen(unittest.TestCase):
    def test_part_one_example(self):
        self.assertEqual(13, part_one(test=True))

    def test_part_one(self):
        self.assertEqual(6272, part_one())

    # def test_part_two_example(self):
    #     pass
    #
    # def test_part_two(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
