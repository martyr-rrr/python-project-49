"""Brain Prime game script."""

from hexlet_code.engine import run
from hexlet_code.games import prime


def main():
    """Run the Prime game."""
    run(prime.DESCRIPTION, prime.generate_round)


if __name__ == '__main__':
    main()
