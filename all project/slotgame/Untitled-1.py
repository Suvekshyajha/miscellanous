# Initialize empty board
board = [' ' for _ in range(9)]

def print_board(board):
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-' * 5)

# Check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for combo in win_conditions:
        if all(board[pos] == player for pos in combo):
            return True
    return False

# Simple AI agent
def ai_move(board):
    # 1. Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner(board, 'O'):
                return
            board[i] = ' '  # Undo

    # 2. Block player from winning
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner(board, 'X'):
                board[i] = 'O'  # Block the player
                return
            board[i] = ' '  # Undo

    # 3. Else pick first empty
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            return

# Play the game
def play_game():
    while True:
        print_board(board)
        # Player move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break

        # Check for draw
        if ' ' not in board:
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move(board)
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break

        if ' ' not in board:
            print_board(board)
            print("It's a draw!")
            break

play_game()
