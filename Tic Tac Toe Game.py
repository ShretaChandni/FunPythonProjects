# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True  # Row check
        if all(board[j][i] == player for j in range(3)): return True  # Column check
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True  # Diagonal check
    return False

# Function to check if the board is full (draw)
def is_draw():
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Main game loop
def play_game():
    player = "X"
    while True:
        print_board()
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (1-3 1-3): ").split())
            row, col = row - 1, col - 1  # Convert to 0-based index
            
            if board[row][col] != " ":
                print("Spot already taken! Try again.")
                continue

            board[row][col] = player  # Mark the move
            
            if check_winner(player):
                print_board()
                print(f"Player {player} WINS! 🎉")
                break
            if is_draw():
                print_board()
                print("It's a DRAW! 🤝")
                break

            player = "O" if player == "X" else "X"  # Switch player

        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers between 1 and 3.")

# Start the game
play_game()
