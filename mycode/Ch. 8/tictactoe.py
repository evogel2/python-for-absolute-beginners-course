# create the board
def create_board():
    #    board = [
    #        [r1_c1, r1_c2, r1_c3],
    #        [r2_c1, r2_c2, r2_c3],
    #        [r3_c1, r3_c2, r3_c3]
    #    ]

    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    return board


# until someone wins (check for winner)
#   choose location, mark it
#   toggle active player
def play_round(board, players, symbols, index):
    while not find_winner(board):
        announce_turn(players, index)
        show_board(board)
        if not choose_location(board, symbols[index]):
            print("That isn't a valid play, try again.")
            continue

        index = (index + 1) % len(players)

    winner = players[(index + 1) % len(players)]
    return winner


def announce_turn(players, index):
    player = players[index]
    print(f"It's {player}'s turn! Here's the board:")


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=' | ')
        print()


def choose_location(board, symbol):
    row = int(input("Choose which row:\n")) - 1
    column = int(input("Choose which column:\n")) - 1

    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # Win by rows
    rows = board
    sequences.extend(rows)

    # Win by columns
    columns = []
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx]
        ]
        sequences.append(col)

    # Win by diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    sequences.extend(diagonals)

    return sequences


def main():
    players_list = ['Elliott', 'Computer']
    player_symbols = ['X', 'O']
    active_player_index = 0

    board = create_board()

    winner = play_round(board, players_list, player_symbols, active_player_index)

    # game over!
    print(f"Game over! {winner} has won with the board: ")
    show_board(board)


if __name__ == '__main__':
    main()
