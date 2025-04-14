"""Game engine module."""

import prompt


def run(description, generate_round_func):
    """General game engine logic."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description)

    for _ in range(3):
        question, correct_answer = generate_round_func()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            error_msg = f"'{user_answer}' is wrong answer ;(. "
            error_msg += f"Correct was '{correct_answer}'."
            print(error_msg)
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
