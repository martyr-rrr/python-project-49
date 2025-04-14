"""Calculator game script."""
from hexlet_code.engine import run
from hexlet_code.games.calc import DESCRIPTION, generate_round


def main():
    """Run the calculator game."""
    run(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()
