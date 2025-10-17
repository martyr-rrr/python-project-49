#!/usr/bin/env python3
import random


def calculate_expression(num1, num2, operator):
    """Calculate expression based on operator."""
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case _:
            raise ValueError(f"Unknown operator: {operator}")


def generate_round():
    """Generate a round for calculator game."""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(["+", "-", "*"])

    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate_expression(num1, num2, operator))

    return question, correct_answer
