#!/usr/bin/env python3
import prompt


def welcome_user():
    """Ask user name and greet."""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
