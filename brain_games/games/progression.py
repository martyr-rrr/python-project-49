#!/usr/bin/env python3
import random


def generate_progression(start, step, length):
    """Generate arithmetic progression."""
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    return progression


def generate_round():
    """Generate a round for progression game."""
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    
    return question, correct_answer
