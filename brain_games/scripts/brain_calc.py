#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games import calc


def main():
    """Main function of the Brain Calc game."""
    description = "What is the result of the expression?"
    run_game(calc, description)


if __name__ == "__main__":
    main()
