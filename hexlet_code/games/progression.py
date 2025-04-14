"""Arithmetic progression game module."""

from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    """Generate arithmetic progression."""
    return [start + i * step for i in range(length)]


def generate_round():
    """Generate a round of progression game."""
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint(5, 15)
    progression = generate_progression(start, step, length)

    hidden_index = randint(0, length - 1)
    answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))

    return question, answer
