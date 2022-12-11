import unittest

from day_eleven import part_one, sunday_morning_parsing_routine, get_input, part_two


class TestDayEleven(unittest.TestCase):
    def test_part_one_example(self):
        file = get_input(test=True)
        monkeys = [
            {
                'monkey': 0,
                'items': [79, 98],
                'operation': '*19',
                'divide': 23,
                'test_true': 2,
                'test_false': 3,
                'inspections': 0,
                'worry': 0,
            }, {
                'monkey': 1,
                'items': [54, 65, 75, 74],
                'operation': '+6',
                'divide': 19,
                'test_true': 2,
                'test_false': 0,
                'inspections': 0,
                'worry': 0,
            }, {
                'monkey': 2,
                'items': [79, 60, 97],
                'operation': '*old',
                'divide': 13,
                'test_true': 1,
                'test_false': 3,
                'inspections': 0,
                'worry': 0,
            }, {
                'monkey': 3,
                'items': [74],
                'operation': '+3',
                'divide': 17,
                'test_true': 0,
                'test_false': 1,
                'inspections': 0,
                'worry': 0,
            }
        ]

        self.assertEqual(monkeys, sunday_morning_parsing_routine(file))
        self.assertEqual(10605, part_one(test=True))

    def test_part_one(self):
        self.assertEqual(111210, part_one())

    def test_part_two_example(self):
        self.assertEqual(2713310158, part_two(test=True))

    def test_part_two(self):
        self.assertEqual(15447387620, part_two())


if __name__ == '__main__':
    unittest.main()
