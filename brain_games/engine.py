"""Game engine module."""


import prompt


def run(game_module):
    """Run the game engine.
    Args:
        game_module: Module containing game logic with DESCRIPTION and generate_round()
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.DESCRIPTION)
    for _ in range(3):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").lower()
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
