from enum import Enum

Moves = [
    {
        'name': "Rock",
        'move': ['A', 'X']
    },

    {
        'name': "Paper",
        'move': ['B', 'Y']
    },

    {
        'name': "Scissors",
        'move': ['C', 'Z']
    }
]


class Points(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Score(Enum):
    Win = 6
    Draw = 3
    Lose = 0


round_result: dict[tuple[Points, Points], Score] = {
    (Points.Rock, Points.Rock): Score.Draw,
    (Points.Rock, Points.Paper): Score.Win,
    (Points.Rock, Points.Scissors): Score.Lose,
    (Points.Paper, Points.Rock): Score.Lose,
    (Points.Paper, Points.Paper): Score.Draw,
    (Points.Paper, Points.Scissors): Score.Win,
    (Points.Scissors, Points.Rock): Score.Win,
    (Points.Scissors, Points.Paper): Score.Lose,
    (Points.Scissors, Points.Scissors): Score.Draw,
}


def get_input():
    input_file = 'input.txt'

    file = open(input_file, mode='r')

    return file


def calculate_score(opponent_points, my_points):
    return my_points.value + round_result[opponent_points, my_points].value


def calculate_score_with_strategy(opponent_move, my_move):
    rock = Points.Rock.name
    paper = Points.Paper.name
    scissors = Points.Scissors.name

    if opponent_move == rock:
        if my_move == rock:
            return Score.Lose.value + Points.Scissors.value

        if my_move == paper:
            return Score.Draw.value + Points.Rock.value

        if my_move == scissors:
            return Score.Win.value + Points.Paper.value

    if opponent_move == paper:
        if my_move == rock:
            return Score.Lose.value + Points.Rock.value

        if my_move == paper:
            return Score.Draw.value + Points.Paper.value

        if my_move == scissors:
            return Score.Win.value + Points.Scissors.value

    if opponent_move == scissors:
        if my_move == rock:
            return Score.Lose.value + Points.Paper.value

        if my_move == paper:
            return Score.Draw.value + Points.Scissors.value

        if my_move == scissors:
            return Score.Win.value + Points.Rock.value

    return 0


def matches(match, with_strategy=False):
    opponent, me = match.rstrip("").rstrip(" ").rstrip("\n").split(" ")

    opponent_move = next(move['name'] for move in Moves if opponent in move['move'])
    my_move = next(move['name'] for move in Moves if me in move['move'])

    if with_strategy:
        return calculate_score_with_strategy(opponent_move, my_move)

    return calculate_score(Points[opponent_move], Points[my_move])


def total_score(file, with_strategy=False):
    return sum(matches(match, with_strategy=with_strategy) for match in file)


if __name__ == '__main__':
    print('Part 1:', total_score(get_input()))
    print('Part 2:', total_score(get_input(), with_strategy=True))
