def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]
    return None

def play_game():
    board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        if board[row][col] == "-":
            board[row][col] = player
            winner = check_win(board)
            if winner:
                print_board(board)
                print(f"{winner} wins!")
                break
            if all([cell != "-" for row in board for cell in row]):
                print_board(board)
                print("Tie!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That space is taken. Try again.")

if __name__ == "__main__":
    play_game()
