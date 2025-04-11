from random import randint

DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."

def is_even(number):
    return number % 2 == 0

def generate_round():
    number = randint(1, 100)
    question = str(number)
    answer = 'yes' if is_even(number) else 'no'
    return question, answer
