# 20x2 Dice Game

## Overview

This is a Python-based 20x2 board game where a human player competes against the computer. Both players roll a dice, and the first one to reach or pass the 20th position on the board wins the game. The game includes special black holes that will reset a player's position when landed upon. The game results are also saved to a text file, allowing players to view their game statistics.

## Game Rules

1. **Starting the Game**: Both the human and computer must roll a 6 to start the game.
2. **Dice Roll**: Players roll a dice to move forward on the board. The number rolled is halved and added to the player's position.
3. **Black Holes**: If a player lands on positions 7 or 14, they hit a black hole, resetting their position to 1.
4. **Winning Condition**: The first player to reach or pass position 20 wins the game.

## Features

- **Interactive Gameplay**: Players roll the dice interactively by pressing enter.
- **Game Board Display**: After every turn, the game board is displayed showing the positions of both the human and computer players.
- **Black Hole Traps**: Players who land on positions 7 or 14 are sent back to the starting position.
- **Game Result Recording**: The game details, including the number of moves, black hole hits, and winner, are saved to a text file.

## How to Run

### Prerequisites

- Python 3.x
- Install the required `prettytable` module:
  ```bash
  pip install prettytable
