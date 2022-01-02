import random
import prompt
from brain_games.greeting import greeting
from brain_games.correct_answer import correct_answer
from brain_games.wrong_answer import wrong_answer
from brain_games.congratulations import congrantulations
from brain_games.gcd import gcd


def game() -> None:
    name = greeting('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        print(f'Question: {first_number} {second_number}')
        answer = prompt.string('Your answer: ')
        result = gcd(first_number, second_number)
        if int(answer) == result:
            correct_answer()
        else:
            wrong_answer(name, result, answer)
            return

    congrantulations(name)
