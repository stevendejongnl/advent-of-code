import unittest

from day_two import matches, total_score
from io import TextIOWrapper, BytesIO


class TestDayTwo(unittest.TestCase):
    def test_part_one(self):
        input = b"A Y\n"\
                b"B X\n"\
                b"C Z"
        file = TextIOWrapper(BytesIO(input))

        score_match_one = matches("A Y")
        score_match_two = matches("B X")
        score_match_three = matches("C Z")
        total_score_result = total_score(file)

        self.assertEqual(8, score_match_one)
        self.assertEqual(1, score_match_two)
        self.assertEqual(6, score_match_three)
        self.assertEqual(15, total_score_result)


if __name__ == '__main__':
    unittest.main()
