#!/usr/bin/env python3
import random


def is_prime(number):
    """Check if number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    """Generate a round for prime game."""
    number = random.randint(1, 100)
    
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    
    return question, correct_answer
