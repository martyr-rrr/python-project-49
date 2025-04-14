"""Game engine module."""

import sys

def run(description, generate_round_func):
    """Game engine implementation that exactly matches test expectations."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(description)

    for _ in range(3):
        question, correct_answer = generate_round_func()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer != correct_answer.lower():
            print(f"'{user_answer}' is wrong answer ;(. Correct was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            sys.exit(0)

        print("Correct!")

    print(f"Congratulations, {name}!")
