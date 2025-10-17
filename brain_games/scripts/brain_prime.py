#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games import prime


def main():
    """Main function of the Brain Prime game."""
    description = (
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
    run_game(prime, description)


if __name__ == '__main__':
    main()
