from typing import Any, Text


def wrong_answer(
    name: Text,
    correct_answer: Any,
    wrong_answer_text: Any
) -> None:
    print(
        f"'{wrong_answer_text}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'."
    )
    print(f"Let's try again, {name}!")
