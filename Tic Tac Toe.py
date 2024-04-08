import random
import sys

def check_winner(board, current_player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]
    
    return None
    
def game():
    board = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]

    # Define the players
    players = ['X', 'O']

    # Define the current player
    current_player = random.choice(players)

    # Start the game loop
    while True:

        # Display the board
        print(board)

        # Get the player's move
        while True:
            row = int(input("Enter the row number: "))
            if row not in range(0,3):
                print('index out of range')
            else:
                break


        while True:
            column = int(input("Enter the column number: "))
            if column not in range(0,3):
                print('index out of range')
            else:
                break

        # Check if the space is already occupied
        if board[row][column] != '-':
            print('Space already occupied.')
            continue

        # Make the move
        board[row][column] = current_player

        # Check if the game is over
        winner = check_winner(board, current_player)
        if winner:
            print(winner + ' wins!')
            break

        # Switch players
        current_player = players[players.index(current_player) ^ 1]
    return board

#create a restart game function
def restart():
     #restart game
     game()

def main():
    # Display the winner
    game()
    print('Do you want to restart game? (Y/N)')
    answer = input("answer: ")
    answer.lower()
    if 'y' in answer:
        restart()
    else:
        sys.exit()

main()
