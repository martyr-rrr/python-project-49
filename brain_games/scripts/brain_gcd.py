"""GCD game script."""
from brain_games.engine import run
from brain_games.games.gcd import DESCRIPTION, generate_round


def main():
    """Run the GCD game."""
    run(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()
