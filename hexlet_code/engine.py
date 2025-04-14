"""Game engine module."""


import sys
from functools import partial


def run(description, generate_round_func):
    """General game engine logic."""
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print(description)

    for _ in range(3):
        question, correct_answer = generate_round_func()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
