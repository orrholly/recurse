# coding=utf-8
# **************************************************************
# Program: tic_tac_toe.py
# Author: Holly Orr
# Date: 10/24/2017
#
# Description:
# write a program that lets two humans play a game of Tic Tac Toe in a terminal. The program should let the players take
# turns to input their moves. The program should report the outcome of the game.

# Improvements:  added support for a computer player to your game.
#
# For later: make the AI smarter
# **************************************************************

import random

# **************************************************************
# GLOBAL VARIABLES
# **************************************************************

# set player mode to zero initially to be set to 1 or 2 by user
player_mode = 0
player1_gamepiece = ""
player2_gamepiece = ""
turn = ""

# create gameboard list variable with 9 ints
gameboard = range(9)

# for error checking that the chosen spot is in range
r = range(9)

# score keeping
player1_score = 0
player2_score = 0

# set global flag to keep or stop playing
go_again = "y"

player_1_name = ""
player_2_name = ""

# **************************************************************
# FUNCTIONS
# **************************************************************

def introduction():
    print "\n"
    print "Let's play tic-tac-toe!"
    global player_mode
    global player1_gamepiece
    global player2_gamepiece
    global turn
    global player_1_name
    global player_2_name
    player_1_name = raw_input("What is your name?: \n")
    while not (player_mode == 1 or player_mode == 2):
        player_mode = convert_to_number(raw_input("Welcome " + player_1_name + ". Will you be playing in 1 or 2 player mode?: \n"))
        if player_mode == 1:
            print "Hello " + player_1_name + ", you have chosen to play the computer. You can call me Hal."
            player_2_name = "Hal"
        elif player_mode == 2:
            print "Hello " + player_1_name + ", you have chosen to play another human."
            player_2_name = raw_input("What is the other human's name?: \n")
    player1_gamepiece, player2_gamepiece = input_player_piece()
    turn = go_first()
    if turn == "player_1":
        print("Congrats " + player_1_name + ". The " + player1_gamepiece + "\'s will go first.")
    else:
        print("Congrats " + player_2_name + ". The " + player2_gamepiece + "\'s will go first.")


def input_player_piece():
    piece = ''
    while not (piece == 'x' or piece == 'o'):
        print
        piece = raw_input(player_1_name + ", do you want to be x or o?" + "\n")
    # if user chooses x, it will be listed first, if chooses o it will be listed first
    if piece == 'x':
        return ['x', 'o']
    else:
        return ['o', 'x']


def go_first():
    # 'flip the coin' for who goes first
    if random.randint(0, 1) == 0:
        return 'player_1'
    else:
        return 'player_2'


def run_game_mode():
    global player_mode
    if player_mode == 1:
        play_game_mode_1()
    else:
        play_game_mode_2()


def play_game_mode_1():
    global go_again
    global turn
    display_game_board()
    while go_again.lower() == "y":
        if turn == 'player_1':
            player1_move()
        else:
            player2_computer_move()


def play_game_mode_2():
    global go_again
    global turn
    display_game_board()
    while go_again.lower() == "y":
        if turn == 'player_1':
            player1_move()
        else:
            player2_move()


def display_game_board():
    print "\n"
    print gameboard[0], "|", gameboard[1], "|", gameboard[2]
    print "---------"
    print gameboard[3], "|", gameboard[4], "|", gameboard[5]
    print "---------"
    print gameboard[6], "|", gameboard[7], "|", gameboard[8]
    print "\n"


def player1_move():
    global player1_gamepiece
    global turn
    while True:
        player1_input = check_number(player_1_name, player1_gamepiece)
        if gameboard[player1_input] != 'x' and gameboard[player1_input] != 'o':
            gameboard[player1_input] = player1_gamepiece
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()
    turn = "player_2"


def player2_move():
    global player2_gamepiece
    global turn
    while True:
        player2_input = check_number(player_2_name, player2_gamepiece)
        if gameboard[player2_input] != 'x' and gameboard[player2_input] != 'o':
            gameboard[player2_input] = player2_gamepiece
            break;
        else:
            print "That spot is already taken!" + "\n"
    display_game_board()
    check_winner()
    turn = "player_1"


def player2_computer_move():
    global player2_gamepiece
    global turn
    global r
    print "It's my turn. I'm thinking.... I just added an " + player2_gamepiece + " to the board."
    block_index = check_block()
    if block_index != 99:
        gameboard[block_index] = player2_gamepiece
    else:
        good_move = False
        while good_move is False:
            computer_input = random.choice(r)
            int_computer_input = int(computer_input)
            if gameboard[int_computer_input] != 'x' and gameboard[int_computer_input] != 'o':
                gameboard[int_computer_input] = player2_gamepiece
                good_move = True
            else:
                good_move = False
    display_game_board()
    check_winner()
    turn = "player_1"


def possible_wins():
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
    possible_plays = [top_row, mid_row, bottom_row, left_col, mid_col, right_col, diag_lr, diag_rl]

    return possible_plays


def check_block():
    winning_blocks = possible_wins()
    for block in winning_blocks:
    unique_number = len(set(block))
    if unique_number == 2:
        for i in range(len(block)):
            if i != 'x' and i != 'o':
                return i
    else:
        return 99


def check_winner():
    # winning rows
    # top_row = [gameboard[0], gameboard[1], gameboard[2]]
    # mid_row = [gameboard[3], gameboard[4], gameboard[5]]
    # bottom_row = [gameboard[6], gameboard[7], gameboard[8]]
    # # winning columns
    # left_col = [gameboard[0], gameboard[3], gameboard[6]]
    # mid_col = [gameboard[1], gameboard[4], gameboard[7]]
    # right_col = [gameboard[2], gameboard[5], gameboard[8]]
    # # winning diagonals
    # diag_lr = [gameboard[0], gameboard[4], gameboard[8]]
    # diag_rl = [gameboard[2], gameboard[4], gameboard[6]]
    #
    # # list of all winning combination lists
    # winning_combos = [top_row, mid_row, bottom_row, left_col, mid_col, right_col, diag_lr, diag_rl]

    winning_combos = possible_wins()

    for combo in winning_combos:
        is_winner = all(combo[0] == item for item in combo)
        if is_winner is True:
            if player1_gamepiece in combo:
                print "The " + player1_gamepiece + "'s win! Congratulations " + player_1_name + "!"
                global player1_score
                player1_score += 1
                play_again()
            elif player2_gamepiece in combo:
                print "The " + player2_gamepiece + "'s win! Congratulations " + player_2_name + "!"
                global player2_score
                player2_score += 1
                play_again()
    is_tied = all(isinstance(x, str) for x in gameboard)
    if is_tied is True:
        print "It's a tie!"
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
    print player_1_name + ": " + str_player1_score
    print player_2_name + ": " + str_player2_score
    print "-------------------"
    print "\n"
    # ask if want to play again
    go_again = raw_input("Would you like to play again? Enter y or n:" + "\n")
    while go_again.lower() != "n" and go_again.lower() != "y":
        go_again = raw_input("You must enter y or n:" + "\n")

    if go_again.lower() == "y":
        global gameboard
        global player_mode
        gameboard = range(9)
        print "Great! Let's keep playing!"
        run_game_mode()
    else:
        print "Thanks for playing!"
        exit()


def check_number(player, symbol):
    passed = False
    while passed is False:
        entered_player = raw_input(player + ", enter the number on the board where you want to place an " + symbol + ": \n")
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
    run_game_mode()


if __name__ == "__main__":
    main()