"""Game engine module."""

import sys
from functools import partial  # noqa: F401


def run(description, generate_round_func, input_func=input):
    """General game engine logic."""
    print('Welcome to the Brain Games!')
    name = input_func('May I have your name? ').strip()
    print(f'Hello, {name}!')
    print(description)

    for _ in range(3):
        question, correct_answer = generate_round_func()
        print(f'Question: {question}')
        user_answer = input_func('Your answer: ').strip()

        if user_answer.lower() != correct_answer.lower():
            error_msg = f"'{user_answer}' is wrong answer ;(. "
            error_msg += f"Correct was '{correct_answer}'."
            print(error_msg)
            print(f"Let's try again, {name}!")
            sys.exit(0)

        print('Correct!')

    print(f'Congratulations, {name}!')
