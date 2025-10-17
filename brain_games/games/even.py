#!/usr/bin/env python3
import random


def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def generate_round():
    """Generate a round for even game."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
