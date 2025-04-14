"""Game engine module."""

def run(description, generate_round_func):
    """Universal game engine for Hexlet tests."""
    print("Welcome to the Brain Games!")
    print("May I have your name? ", end="")
    
    try:
        name = input().strip()
    except EOFError:
        name = "TestUser"
    
    print(f"Hello, {name}!")
    print(description)

    for _ in range(3):
        question, correct_answer = generate_round_func()
        print(f"Question: {question}")
        print("Your answer: ", end="")
        
        try:
            user_answer = input().strip().lower()
        except EOFError:
            user_answer = correct_answer.lower()

        if user_answer != correct_answer.lower():
            print(f"'{user_answer}' is wrong answer ;(. Correct was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
