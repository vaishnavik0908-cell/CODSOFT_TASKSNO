# Tic-Tac-Toe AI using Minimax

board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_board_full():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def player_move():
    while True:
        try:
            position = int(input("Enter your move (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            position -= 1

            if board[position] != " ":
                print("That position is already occupied. Try again.")
                continue

            board[position] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


def play_game():
    print("Welcome to Tic-Tac-Toe AI!")
    print("You are X and the AI is O.")
    print("Choose a position from 1 to 9.")

    while True:
        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("Congratulations! You won!")
            break

        if is_board_full():
            print_board()
            print("It's a draw!")
            break

        ai_move()

        print("AI has made its move.")

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

        if is_board_full():
            print_board()
            print("It's a draw!")
            break


play_game()