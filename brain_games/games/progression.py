import random
import prompt
from brain_games.greeting import greeting
from brain_games.correct_answer import correct_answer
from brain_games.wrong_answer import wrong_answer
from brain_games.congratulations import congrantulations


def game() -> None:
    name = greeting('What number is missing in the progression?')
    progressions = [
        [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],
        [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],
        [14, 19, 24, 29, 34, 39, 44, 49, 54, 59],
        [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
        [4, 7, 10, 13, 16, 19, 22, 25, 28, 31],
        [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
        [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
        [5, 9, 13, 17, 21, 25, 29, 33, 37, 41],
    ]
    for _ in range(3):
        progression = random.choice(progressions)
        hidden_item_index = random.randint(0, len(progression) - 1)
        question = ''
        i = 0
        while i < len(progression):
            if i == hidden_item_index:
                question += '.. '
                i += 1
                continue
            question += f'{progression[i]} '
            i += 1
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        result = progression[hidden_item_index]
        if int(answer) == result:
            correct_answer()
        else:
            wrong_answer(name, result, answer)
            return

    congrantulations(name)
