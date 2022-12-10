import unittest

from day_ten import part_one, part_two


class TestDayTen(unittest.TestCase):
    def test_part_one_example(self):
        self.assertEqual(13140, part_one(test=True))

    def test_part_one(self):
        self.assertTrue(22000 > part_one())
        self.assertEqual(16060, part_one())

    def test_part_two_example(self):
        self.assertEqual("""
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""", part_two(test=True)[0])

    def test_part_two(self):
        self.assertEqual("""
###...##...##..####.#..#.#....#..#.####.
#..#.#..#.#..#.#....#.#..#....#..#.#....
###..#..#.#....###..##...#....####.###..
#..#.####.#....#....#.#..#....#..#.#....
#..#.#..#.#..#.#....#.#..#....#..#.#....
###..#..#..##..####.#..#.####.#..#.#....""", part_two()[0])

        # https://www.reddit.com/r/adventofcode/comments/zhl2wl/comment/izmt9o6/?utm_source=reddit&utm_medium=web2x&context=3
        self.assertEqual("""
███...██...██..████.█..█.█....█..█.████.
█..█.█..█.█..█.█....█.█..█....█..█.█....
███..█..█.█....███..██...█....████.███..
█..█.████.█....█....█.█..█....█..█.█....
█..█.█..█.█..█.█....█.█..█....█..█.█....
███..█..█..██..████.█..█.████.█..█.█....""", part_two()[1])


if __name__ == '__main__':
    unittest.main()
