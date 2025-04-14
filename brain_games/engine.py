"""Game engine module."""
import prompt


def run(description, generate_round_func):
    """Run the game engine."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)
    
    for _ in range(3):
        question, correct_answer = generate_round_func()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").lower()

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
