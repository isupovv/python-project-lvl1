import random
import prompt
from brain_games.greeting import greeting
from brain_games.correct_answer import correct_answer
from brain_games.is_prime import is_prime
from brain_games.wrong_answer import wrong_answer
from brain_games.congratulations import congrantulations


def game() -> None:
    name = greeting(
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
    for _ in range(3):
        number = random.randint(2, 31)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        result = is_prime(number)
        if answer.lower() == result:
            correct_answer()
        else:
            wrong_answer(name, result, answer)
            return

    congrantulations(name)
