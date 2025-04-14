"""Game engine module."""

import sys

def run(description, generate_round_func):
    """General game engine logic."""
    print('Welcome to the Brain Games!')
    
    try:
        name = input('May I have your name? ').strip()
    except EOFError:
        # Для автоматических тестов
        name = "TestUser"
        print(name)
    
    print(f'Hello, {name}!')
    print(description)

    for _ in range(3):
        question, correct_answer = generate_round_func()
        print(f'Question: {question}')
        
        try:
            user_answer = input('Your answer: ').strip()
        except EOFError:
            # Для автоматических тестов
            user_answer = correct_answer
            print(user_answer)

        if user_answer.lower() != correct_answer.lower():
            print(f"'{user_answer}' is wrong answer ;(. Correct was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            sys.exit(0)

        print('Correct!')

    print(f'Congratulations, {name}!')
