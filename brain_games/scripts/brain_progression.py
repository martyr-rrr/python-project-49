#!/usr/bin/env python
"""Brain Progression game script."""
from brain_games.engine import run
from brain_games.games.progression import DESCRIPTION, generate_round

def main():
    """Run the Progression game."""
    run(DESCRIPTION, generate_round)

if __name__ == '__main__':
    main()
