#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games import progression


def main():
    """Main function of the Brain Progression game."""
    description = 'What number is missing in the progression?'
    run_game(progression, description)


if __name__ == '__main__':
    main()
