"""Even number game logic."""

from random import randint

DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."

def is_even(number):
    """Check if number is even."""
    return number % 2 == 0

def generate_round():
    """Generate question-answer pair."""
    number = randint(1, 100)
    return str(number), 'yes' if is_even(number) else 'no'
