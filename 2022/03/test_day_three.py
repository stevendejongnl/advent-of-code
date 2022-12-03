import unittest

from day_three import split_into_compartments, shared_item, priority, sum_priorities, get_rucksack_groups, \
    group_shared_item


class TestDayThree(unittest.TestCase):
    def test_part_one(self):
        first_rucksack = split_into_compartments("vJrwpWtwJgWrhcsFMMfFFhFp")
        second_rucksack = split_into_compartments("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
        shared_item_in_rucksack = shared_item(second_rucksack)
        priority_of_uppercase_s = priority()['uppercase']['S']

        priorities = [
            16, 38, 42, 22, 20, 19
        ]
        total_priority_of_all_rucksacks = sum_priorities(priorities)

        self.assertEqual(("vJrwpWtwJgWr", "hcsFMMfFFhFp"), first_rucksack)
        self.assertEqual('L', shared_item_in_rucksack)
        self.assertEqual(45, priority_of_uppercase_s)
        self.assertEqual(157, total_priority_of_all_rucksacks)

    def test_part_two(self):
        groups = get_rucksack_groups([
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ])
        shared_item_in_rucksack = group_shared_item(groups[0])

        priorities = [
            18, 52
        ]
        total_priority_of_item_types = sum_priorities(priorities)

        self.assertEqual([
            (
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg"
            ),
            (
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw"
            )
        ], groups)
        self.assertEqual('r', shared_item_in_rucksack)
        self.assertEqual(70, total_priority_of_item_types)


if __name__ == '__main__':
    unittest.main()
