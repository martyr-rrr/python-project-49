#!/usr/bin/env python3
import random
import prompt


def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def play_even_game():
    """Play the even number game."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers_needed = 3
    correct_answers = 0
    
    while correct_answers < correct_answers_needed:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = input('Your answer: ').strip().lower()
        
        correct_answer = 'yes' if is_even(number) else 'no'
        
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')


def main():
    """Main function of the Brain Even game."""
    play_even_game()


if __name__ == '__main__':
    main()
