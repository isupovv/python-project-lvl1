import prompt
import random
from brain_games.greeting import greeting
from brain_games.correct_answer import correct_answer
from brain_games.wrong_answer import wrong_answer
from brain_games.congratulations import congrantulations


def game() -> None:
    name = greeting('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2:
            if answer.lower() == 'no':
                correct_answer()
            else:
                wrong_answer(name, 'no', 'yes')
                return
        else:
            if answer.lower() == 'yes':
                correct_answer()
            else:
                wrong_answer(name, 'yes', 'no')
                return
    congrantulations(name)
