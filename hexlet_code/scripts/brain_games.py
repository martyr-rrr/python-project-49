"""Brain Games main menu script."""

from hexlet_code.engine import run
from hexlet_code.games import even, calc, gcd, prime, progression


GAMES = {
    '1': (even.DESCRIPTION, even.generate_round),
    '2': (calc.DESCRIPTION, calc.generate_round),
    '3': (gcd.DESCRIPTION, gcd.generate_round),
    '4': (prime.DESCRIPTION, prime.generate_round),
    '5': (progression.DESCRIPTION, progression.generate_round)
}


def main():
    """Run main game selection menu."""
    print("Welcome to the Brain Games!")
    print("1. Even/Odd")
    print("2. Calculator")
    print("3. Greatest Common Divisor")
    print("4. Prime Number")
    print("5. Arithmetic Progression")

    choice = input("Select a game (1-5): ")
    if choice not in GAMES:
        print("Invalid choice!")
        return

    description, generate_round = GAMES[choice]
    run(description, generate_round)


if __name__ == '__main__':
    main()
