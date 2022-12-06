import unittest

from day_six import part_one, find_marker, part_two


class TestDaySix(unittest.TestCase):
    def test_part_one_example(self):
        self.assertEqual(part_one(test=True), ('jpqm', 7))
        self.assertEqual(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz'), ('vwbj', 5))
        self.assertEqual(find_marker('nppdvjthqldpwncqszvftbrmjlhg'), ('pdvj', 6))
        self.assertEqual(find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), ('rfnt', 10))
        self.assertEqual(find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), ('zqfr', 11))

    def test_part_one(self):
        result_part_one = part_one()
        print(f'Result of part one: (marker: "{result_part_one[0]}", after characters: {result_part_one[1]})')
        self.assertIsNotNone(result_part_one)

    def test_part_two_example(self):
        self.assertEqual(find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', total_different=14), ('qmgbljsphdztnv', 19))
        self.assertEqual(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', total_different=14), ('vbhsrlpgdmjqwf', 23))
        self.assertEqual(find_marker('nppdvjthqldpwncqszvftbrmjlhg', total_different=14), ('ldpwncqszvftbr', 23))
        self.assertEqual(find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', total_different=14), ('wmzdfjlvtqnbhc', 29))
        self.assertEqual(find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', total_different=14), ('jwzlrfnpqdbhtm', 26))

    def test_part_two(self):
        result_part_two = part_two()
        print(f'Result of part two: (marker: "{result_part_two[0]}", after characters: {result_part_two[1]})')
        self.assertIsNotNone(result_part_two)


if __name__ == '__main__':
    unittest.main()
