import prompt
import random


def game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(0, 99999)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2:
            if answer.lower() == 'no':
                print('Correct!')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                return
        else:
            if answer.lower() == 'yes':
                print('Correct!')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                return
    print(f'Congratulations, {name}!')
