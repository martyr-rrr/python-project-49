"""Calculator game module."""
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def calculate(num1, num2, operator):
    """Calculate expression."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:  # operator == '*'
        return num1 * num2


def generate_round():
    """Generate a round of calculator game."""
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    operator = choice(OPERATORS)
    question = f'{num1} {operator} {num2}'
    answer = str(calculate(num1, num2, operator))
    return question, answer
