# **************************************************************
# Program: tic_tac_toe.py
# Author: Holly Orr
# Date: 10/24/2017
#
# Description:
# write a program that lets two humans play a game of Tic Tac Toe in a terminal. The program should let the players take
# turns to input their moves. The program should report the outcome of the game.

# For later:  add support for a computer player to your game. You can start with random moves and make the AI smarter if
# you have time.
# **************************************************************

# TODO add packages or modules for playing against computer
import random

# **************************************************************
# GLOBAL VARIABLES
# **************************************************************

# create gameboard list variable with 9 ints
gameboard = range(9)

# for error checking that the chosen spot is in range
r = range(9)

# score keeping
player1_score = 0
player2_score = 0

# set global flag to keep or stop playing
go_again = "y"

player_mode = 0

# **************************************************************
# FUNCTIONS
# **************************************************************

def introduction():
    global player_mode
    print "\n"
    print "Let's play tic-tac-toe!"

    # TODO: if adding logic to give option to play computer
    # print "Welcome. Will you be playing in 1 or 2 player mode?"
    player_mode = raw_input("Would you like to play in 1 or 2 player mode? Enter 1 or 2:" + "\n")


def play_game():
    global go_again
    display_game_board()
    # TODO conditional player mode
    if player_mode == "2":
        while go_again.lower() == "y":
            player1_move()
            player2_move()
    elif player_mode == "1":
        while go_again.lower() == "y":
            player1_move()
            player_computer_move()
        # TODO player_computer_move()

def display_game_board():
    print "\n"
    print gameboard[0], "|", gameboard[1], "|", gameboard[2]
    print "---------"
    print gameboard[3], "|", gameboard[4], "|", gameboard[5]
    print "---------"
    print gameboard[6], "|", gameboard[7], "|", gameboard[8]
    print "\n"


def player1_move():
    while True:
        player1_input = check_number("Player 1", "x")
        if gameboard[player1_input] != 'x' and gameboard[player1_input] != 'o':
            gameboard[player1_input] = 'x'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()


def player2_move():
    while True:
        player2_input = check_number("Player 2", "o")
        if gameboard[player2_input] != 'x' and gameboard[player2_input] != 'o':
            gameboard[player2_input] = 'o'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()

def player_computer_move():
    while True:
       computer_random_choice()
    display_game_board()
    check_winner()


def computer_random_choice():
    computer_move = random.choice(gameboard)
    good_move = False
    while good_move is False:
        if gameboard[computer_move] != 'x' and gameboard[computer_move] != 'o':
            good_move = True
            gameboard[computer_move] = 'o'
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()

def check_winner():
    # winning rows
    top_row = [gameboard[0], gameboard[1], gameboard[2]]
    mid_row = [gameboard[3], gameboard[4], gameboard[5]]
    bottom_row = [gameboard[6], gameboard[7], gameboard[8]]
    # winning columns
    left_col = [gameboard[0], gameboard[3], gameboard[6]]
    mid_col = [gameboard[1], gameboard[4], gameboard[7]]
    right_col = [gameboard[2], gameboard[5], gameboard[8]]
    # winning diagonals
    diag_lr = [gameboard[0], gameboard[4], gameboard[8]]
    diag_rl = [gameboard[2], gameboard[4], gameboard[6]]

    # list of all winning combination lists
    winning_combos = [top_row, mid_row, bottom_row, left_col, mid_col, right_col, diag_lr, diag_rl]

    # variables for player1 and player2
    x_win = "x"
    o_win = "o"

    is_tied = all(isinstance(x, str) for x in gameboard)
    if is_tied is True:
        print "It's a tie!"
        play_again()
    else:
        for combo in winning_combos:
            is_winner = all(combo[0] == item for item in combo)
            if is_winner is True:
                if x_win in combo:
                    print "The x's win! Congrats Player 1!"
                    global player1_score
                    player1_score += 1
                    play_again()
                elif o_win in combo:
                    global player2_score
                    player2_score += 1
                    print "The o's win! Congrats Player 2!"
                    play_again()


def play_again():
    # get global variables for scores
    global player1_score
    global player2_score
    global go_again
    str_player1_score = str(player1_score)
    str_player2_score = str(player2_score)
    print "\n"
    print "SCORE:"
    print "-------------------"
    print "PLAYER 1 | PLAYER 2"
    print "   " + str_player1_score + "     |    " + str_player2_score
    print "-------------------"
    print "\n"
    # ask if want to play again
    go_again = raw_input("Would you like to play again? Enter y or n:" + "\n")
    while go_again.lower() != "n" and go_again.lower() != "y":
        go_again = raw_input("You must enter y or n:" + "\n")

    if go_again.lower() == "y":
        global gameboard
        gameboard = range(9)
        print "Great! Let's keep playing!"
        play_game()
    else:
        print "Thanks for playing!"
        exit()

# error checking logic

def check_number(player, symbol):
    passed = False
    while passed is False:
        entered_player = raw_input(player + ", it's your turn. Enter the number on the board where you want to place an " + symbol + ": \n")
        int_done = convert_to_number(entered_player)
        passed = test_range(int_done)
    return int_done


def convert_to_number(validate_int):
    result = None
    int_converted = validate_int
    while result is None:
        try:
            int_converted = int(int_converted)
            result = int_converted
        except ValueError:
            int_converted = raw_input("You have not entered a numeric value. Try again:  " + "\n")
    return int_converted


def test_range(user_int):
    if user_int not in r:
        print "You have not entered a spot by it number between 0 - 8. "
        return False
    else:
        return True


def main():
    introduction()
    play_game()


if __name__ == "__main__":
    main()