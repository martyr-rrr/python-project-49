"""Game engine module."""

import sys

def run(description, generate_round_func):
    """Universal game engine that works both interactively and in tests."""
    print('Welcome to the Brain Games!')
    
    try:
        name = input().strip()  # Простое чтение ввода без приглашения
        print(f'Hello, {name}!')
    except EOFError:
        name = "TestUser"
        print(f'Hello, {name}!')
    
    print(description)

    for _ in range(3):
        question, correct_answer = generate_round_func()
        print(question)
        
        try:
            user_answer = input().strip().lower()
        except EOFError:
            user_answer = correct_answer.lower()
            print(user_answer)

        if user_answer != correct_answer.lower():
            print(f"'{user_answer}' is wrong answer ;(. Correct was '{correct_answer}'.")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
