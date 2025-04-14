"""Greatest Common Divisor game module."""
from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    """Generate a round of GCD game."""
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    answer = str(gcd(num1, num2))
    return question, answer
