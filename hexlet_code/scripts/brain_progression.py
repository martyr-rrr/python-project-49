"""Brain Progression game script."""

from hexlet_code.engine import run
from hexlet_code.games import progression


def main():
    """Run the Progression game."""
    run(progression.DESCRIPTION, progression.generate_round)


if __name__ == '__main__':
    main()
