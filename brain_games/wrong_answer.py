from typing import Any, Text


def wrong_answer(name: Text, correct_answer: Any, wrong_answer: Any) -> None:
    print(f"'{wrong_answer}' is wrong answer ;(. ' \
    'Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")
