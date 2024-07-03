# this is a main file for the tic-tac-toe project for the Codecademy milestome terminal project
from random import randint
print("Hello")
game_dict = {x:" " for x in range(1, 10)}


def game_start():
    print("Welcome to my tic-tac-toe game!")
    game_update()
    

def game_update():
    game_board = f"""
        | {game_dict[1]} | {game_dict[2]} | {game_dict[3]} |
        |---|---|---|
        | {game_dict[4]} | {game_dict[5]} | {game_dict[6]} |
        |---|---|---|
        | {game_dict[7]} | {game_dict[8]} | {game_dict[9]} |
        """
    print(game_board)


def user_move():
    print("Please, type in a number between 1 and 9: ")
    str_move = input()
    move = int(str_move)

    if check_move(move):
        game_dict[move] = 'X'
        game_update()
    else:
        print("Invalid value or  the cell is already taken. Try again!")
        user_move()


def computer_move():
    move = randint(1, 10)

    if check_move(move):
        game_dict[move] = '0'
        game_update()
    else:
        computer_move()


def check_move(move):
    if move > 0 and move < 10 and game_dict[move] == " ":
        return True
    else:
        return False
    

def check_win():
    target_values = ["X", "O"]
    for target_value in target_values:
        for i in range(3):
            # Horizontal check
            if (
                game_dict[3 * i + 1] == game_dict[3 * i + 2] == game_dict[3 * i + 3] == target_value
            ):
                return True
            # Vertical check
            if (
                game_dict[i + 1] == game_dict[i + 4] == game_dict[i + 7] == target_value
            ):
                return True
        # Diagonal check
        if (
            game_dict[1] == game_dict[5] == game_dict[9] == target_value
        ) or (
            game_dict[3] == game_dict[5] == game_dict[7] == target_value
        ):
            return True
    return False

def play_again():
    print("Would you like to play again? Y/N")
    play = input()
    return play.lower() == "y"

def game_reset():
    global game_dict
    game_dict = {x: " " for x in range(1, 10)}
    game_update()

game_start()

while True:
    while True:
        user_move()
        if check_win():
            print("You won!")
            break
        if " " not in game_dict.values():
            print("Game Over! It's a draw!")
            break
        else:
            print("Now it is the computer's turn!")
            computer_move()
            if check_win():
                print("Computer Won!")
                break
        if " " not in game_dict.values():
            print("Game Over!")
            break

    if play_again():
        game_reset()
        continue
    else:
        break




 
