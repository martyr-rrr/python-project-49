#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games import gcd


def main():
    """Main function of the Brain GCD game."""
    description = 'Find the greatest common divisor of given numbers.'
    run_game(gcd, description)


if __name__ == '__main__':
    main()
