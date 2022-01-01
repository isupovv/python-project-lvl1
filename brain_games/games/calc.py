import prompt
import random
from brain_games.greeting import greeting
from brain_games.correct_answer import correct_answer
from brain_games.wrong_answer import wrong_answer
from brain_games.congratulations import congrantulations


def game() -> None:
    name = greeting('What is the result of the expression?')
    for _ in range(3):
        first_number = random.randint(0, 40)
        second_number = random.randint(0, 40)
        operation = random.choice(['+', '-', '*'])
        result = 0
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        else:
            result = first_number * second_number
        print(f'Question: {first_number} {operation} {second_number}')
        answer = prompt.string('Your answer: ')
        if int(answer) == result:
            correct_answer()
        else:
            wrong_answer(name, result, answer)
            return
    congrantulations(name)
