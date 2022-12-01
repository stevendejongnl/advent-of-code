input_file = 'input.txt'

file = open(input_file, mode='r')

elf_calories: list = []

calories_carried_by_elf = 0
for calories in file:
    if calories != '' and calories != '\n':
        calories_carried_by_elf += int(calories)
    else:
        elf_calories.append(calories_carried_by_elf)
        calories_carried_by_elf = 0

highest_calories = max(elf_calories)
elf_with_highest_calories = elf_calories.index(highest_calories) + 1

print('Highest Calories: ', highest_calories)
print('By Elf: ', elf_with_highest_calories)


# Part two

sort_by_highest_calories = sorted(((value, index) for index, value in enumerate(elf_calories)), reverse=True)
top_three = sort_by_highest_calories[0:3]
print('Top 3 highest calories', top_three)

total_of_top = 0
for calories, elf in top_three:
    total_of_top += calories
print('Total of top 3', total_of_top)
