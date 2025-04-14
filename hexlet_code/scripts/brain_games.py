"""Brain Games main script."""

from hexlet_code.engine import run
from hexlet_code.games import even


def main():
    """Run the Even game by default."""
    run(even.DESCRIPTION, even.generate_round)


if __name__ == '__main__':
    main()
