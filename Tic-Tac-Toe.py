# Tic-Tac-Toe

# Create an empty board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
        print('-------------')

# Function to check if a player has won
def check_win(player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for positions in winning_positions:
        if all(board[p] == player for p in positions):
            return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board()
        position = int(input("Player {}'s turn. Enter a position (1-9): ".format(current_player)))
        if board[position - 1] != ' ':
            print("Invalid move. Position already taken.")
            continue
        board[position - 1] = current_player
        if check_win(current_player):
            print_board()
            print("Player {} wins!".format(current_player))
            break
        if ' ' not in board:
            print_board()
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
