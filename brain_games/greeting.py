import prompt
from typing import Text


def greeting(rules: Text) -> Text:
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    return name
