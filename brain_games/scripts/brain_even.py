#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games import even


def main():
    """Main function of the Brain Even game."""
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(even, description)


if __name__ == "__main__":
    main()
