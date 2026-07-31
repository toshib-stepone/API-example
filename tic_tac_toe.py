"""
Simple two-player Tic Tac Toe (console).
Player 1 = X, Player 2 = O. Enter a position 1-9 as shown on the board.
"""

board = [str(i) for i in range(1, 10)]  # positions 1-9


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combos)


def is_board_full():
    return all(cell in ("X", "O") for cell in board)


def get_move(player):
    while True:
        choice = input(f"Player {player}, enter position (1-9): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Invalid input. Enter a number between 1 and 9.")
            continue
        pos = int(choice) - 1
        if board[pos] in ("X", "O"):
            print("That spot is already taken. Try again.")
            continue
        return pos


def play_game():
    current_player = "X"
    print_board()

    while True:
        pos = get_move(current_player)
        board[pos] = current_player
        print_board()

        if check_winner(current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if is_board_full():
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()