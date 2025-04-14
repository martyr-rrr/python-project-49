#!/usr/bin/env python
"""Brain Prime game script."""
from brain_games.engine import run
from brain_games.games import prime

def main():
    """Run the Prime game."""
    run(prime.DESCRIPTION, prime.generate_round)

if __name__ == '__main__':
    main()
