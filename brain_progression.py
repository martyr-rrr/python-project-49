#!/usr/bin/env python
"""Brain progression game script."""
from brain_games.engine import run
from brain_games.games.progression import generate_round, DESCRIPTION

def main():
    run(generate_round, DESCRIPTION)

if __name__ == '__main__':
    main()
