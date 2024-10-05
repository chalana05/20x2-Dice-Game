import random
from datetime import datetime
from prettytable import PrettyTable


# function to return a random number between 1 and 6
def roll_dice():
    return random.randint(1, 6)


def move_pawn(position, dice_value):
    half_dice_value = dice_value // 2
    new_position = position + half_dice_value
    return new_position


# function to display game board
def display_board(player_pos, computer_pos):
    table = PrettyTable()
    table.field_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                         "18", "19", "20"]
    player_row = ["x" if i == player_pos else "O" if i in [7, 14] else "" for i in range(1, 21)]
    computer_row = ["x" if i == computer_pos else "O" if i in [7, 14] else "" for i in range(1, 21)]
    table.add_row(player_row)
    table.add_row(computer_row)
    print(table)


# function to write a text file
# def write_to_file(player_pos, computer_pos):


# start the game
player_pos = 0
computer_pos = 0
log = 0
winner = ""

# function to the print name
name = str(input("Please enter your name : "))
print("Hi!", name, "WELCOME to the Game")


# function to play the game
def game():
    player_pos = 0
    computer_pos = 0

    while player_pos < 20 and computer_pos < 20:
        print("\n--------------------------------------------------------------------------------------------")
        input("Press enter to roll the dice...")
        dice = roll_dice()
        # player start
        print("player rolled : ", dice)
        if player_pos == 0 and dice == 6:
            player_pos = 1
            print("(...Player entered the board...)")
        elif player_pos > 0:
            player_pos = move_pawn(player_pos, dice)
            if player_pos in [7, 14]:
                player_pos = 1
                print(f"Player hit a black hole and moved back to position {player_pos}.")
            elif player_pos >= 20:
                print(f"Player won the game !!!\n")

                break

        dice = roll_dice()
        # computer start
        print("computer rolled : ", dice)
        if computer_pos == 0 and dice == 6:
            computer_pos = 1
            print("(...Computer entered the board...)")
        elif computer_pos > 0:
            computer_pos = move_pawn(computer_pos, dice)

            if computer_pos in [7, 14]:
                computer_pos = 1
                print(f"Computer hit a black hole and moved back to position {computer_pos}.")
            elif computer_pos >= 20:
                print(f"Computer won the game !!!\n")

                break

        display_board(player_pos, computer_pos)
        # write_to_file(player_pos, computer_pos)

    now = datetime.now()
    d = now.strftime("%Y_%m_%d_%H_%M")
    # above date will return as YYYY_M_D_H_M format
    f = 0
    with open(d + ".txt", "w") as f:
        f.write("Player\n")
        f.write(f"Player moves : {player_pos}\n")
        f.write(f"Black hole hits : {log}\n")
        if player_pos >= 20:
            f.write("Won the game.\n\n")
        else:
            player_pos != 20
            f.write("Lost the game.\n\n")
        f.write("Computer\n")
        f.write(f"Computer moves : {computer_pos}\n")
        f.write(f"Black hole hits : {log}\n")
        if computer_pos >= 20:
            f.write("Won the game.\n")
        else:
            f.write("Lost the game.\n")


game()