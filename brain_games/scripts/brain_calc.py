"""Calculator game script."""
from brain_games.engine import run
from brain_games.games.calc import DESCRIPTION, generate_round


def main():
    """Run the calculator game."""
    run(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()
