import unittest
from day_eleven import part_one, sunday_morning_parsing_routine, get_input, calculate_worried_levels


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
            }, {
                'monkey': 1,
                'items': [54, 65, 75, 74],
                'operation': '+6',
                'divide': 19,
                'test_true': 2,
                'test_false': 0,
            }, {
                'monkey': 2,
                'items': [79, 60, 97],
                'operation': '*old',
                'divide': 13,
                'test_true': 1,
                'test_false': 3,
            }, {
                'monkey': 3,
                'items': [74],
                'operation': '+3',
                'divide': 17,
                'test_true': 0,
                'test_false': 1,
            }
        ]

        self.assertEqual(monkeys, sunday_morning_parsing_routine(file))

        # monkeys_after_throw = calculate_worried_levels(monkeys, 1)
        # self.assertEqual([
        #     [20, 23, 27, 26],
        #     [25, 167, 207, 694, 401, 1046]
        # ], [monkeys_after_throw[0]['items'], monkeys_after_throw[1]['items']])

        monkeys_after_throw = calculate_worried_levels(monkeys, 20)
        self.assertEqual([
            [695, 10, 71, 135, 350],
            [43, 49, 58, 55, 362]
        ], [monkeys_after_throw[0]['items'], monkeys_after_throw[1]['items']])

        self.assertEqual(10605, part_one(test=True))

    def test_part_one(self):
        pass

    def test_part_two_example(self):
        pass

    def test_part_two(self):
        pass


if __name__ == '__main__':
    unittest.main()
