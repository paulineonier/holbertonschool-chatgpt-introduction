def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True

    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == " ":
                        board[row][col] = player
                        break
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input! Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        player = "O" if player == "X" else "X"

    print_board(board)
    if player == "X":
        winner = "O"
    else:
        winner = "X"
    print("Player " + winner + " wins!")

tic_tac_toe()
