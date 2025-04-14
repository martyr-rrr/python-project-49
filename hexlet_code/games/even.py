"""Even number game module."""

from random import randint


DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def generate_round():
    """Generate round for even number game."""
    number = randint(1, 100)
    question = str(number)
    answer = 'yes' if is_even(number) else 'no'
    return question, answer
