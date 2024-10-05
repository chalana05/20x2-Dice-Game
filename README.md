

```markdown
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
  ```

### Steps to Run

1. **Clone or Download the Code**:
   - Clone this repository or download the `20x2_dice_game.py` file.
   
2. **Run the Game**:
   - Open a terminal or command prompt.
   - Navigate to the folder where the game file is located.
   - Run the Python script with the following command:
     ```bash
     python 20x2_dice_game.py
     ```

3. **Play the Game**:
   - Enter your name when prompted.
   - Press enter to roll the dice for each turn.
   - The game will continue until either the human or computer reaches or passes the 20th position.
   - Game results will be printed and also saved to a text file.

### Example Gameplay

```bash
Enter your name here : Alice
Hi Alice welcome to the 20 x 2 game
You will play against the computer.The first one who reach or pass the 20th block will win the game.

Press enter to roll the dice 

+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 5 | 6 | O | 8 | 9 | 10| 11| 12| 13| O | 15| 16| 17| 18| 19| 20|
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| X |   |   |   |   |   | O |   |   |   |   |   |   | O |   |   |   |   |   |   |
| X |   |   |   |   |   | O |   |   |   |   |   |   | O |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

Human dice roll is 4 and current location is 2
Computer dice roll is 5 and current location is 2
```

### Game Result Output

At the end of the game, the results will be saved to a text file named based on the current date and time (e.g., `2024_10_05_12_30.txt`). The file will contain the following information:

```text
Human
Total moves 5
Black hole hits 1
Won the game

Computer
Total moves 4
Black hole hits 2
Lost the game
```

## Code Breakdown

### Functions

1. **`roll_dice()`**: Generates a random dice value between 1 and 6.
2. **`generate_table(human_position, computer_position)`**: Displays the current game board, showing the positions of both the human and the computer.
3. **`text_file()`**: Creates a text file to save the game result, including the number of moves, black hole hits, and the winner.

### Variables

- **`human_position`** and **`computer_position`**: Track the current positions of the human and computer players on the board.
- **`human_moves`** and **`computer_moves`**: Count the number of moves made by each player.
- **`num_of_bh_hits_human`** and **`num_of_bh_hits_computer`**: Track how many times each player hit a black hole.

## Contributing

Feel free to open issues or submit pull requests for improving the game functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This `README.md` file provides instructions and details about the Python game you created. Let me know if you need further modifications or additions!
