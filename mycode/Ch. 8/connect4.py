import copy

# create board
def create_board():
    board = []

    for i in range(6):
        row = []

        for i in range(7):
            cell = None
            row.append(cell)

        board.append(row)

    return board

def print_board(board):
    print("\nHere is the board:")

    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=' | ')
        print()

# until there are 4 in a row (in any direction)
    # play a turn where a player can drop a piece
def play_game(board, players, symbols, index):
    is_winner = False

    while not is_winner:
        print(f"\n{players[index]}, it is your turn!")
        print_board(board)

        move_played = False
        while not move_played:
            selected_column = input(f"Select a column (1-7) to place your symbol '{symbols[index]}':\n")
            if int(selected_column) not in range(1,8):
                print("That is not a valid column! Please enter a number between 1 and 7.")
                continue
            selected_column = int(selected_column) - 1
            move_played = check_move(board, selected_column, symbols[index])

        is_winner = find_winner(board)
        index = (index + 1) % 2

    index = (index + 1) % 2
    print_board(board)
    print()
    print("The game is over!!")
    print(f"The winner is {players[index]}, who got four '{symbols[index]}'s in a row!")

def check_move(board, column, symbol):
    cols = []

    for i in range(7):
        col = []
        for row in range(6):
            col.append(board[row][i])

        cols.append(col)

    if all(cell is not None for cell in cols[column]):
        print(f"Sorry, column #{column + 1} is full! Please choose a different column.")
        print()
        return False

    single_column = cols[column]
    i = len(single_column)-1

    while True:
        if single_column[i] is not None:
            i -= 1
            continue
        else:
            board[i][column] = symbol
            break

    return True

# alternate turns, checking in between in turn
def find_winner(board):
    board2 = copy.deepcopy(board)
    sequences = []

    # rows
    rows = board2
    sequences.extend(copy.deepcopy(rows))

    # columns
    cols = []
    for i in range(7):
        col = []
        for row in range(6):
            col.append(board2[row][i])

        cols.append(col)
    sequences.extend(copy.deepcopy(cols))

    # diags
    diags = []
    # down-right
    for j in range(len(board2)):
        for x in range(len(board2)):
            diagdown = []
            y = j
            for i in range(6):
                try:
                    diagdown.append(board2[x][y])
                    x += 1
                    y += 1
                except:
                    pass
            diags.append(diagdown)

    # up-right
    for j in range(len(board2)):
        for x in range(len(board2)):
            diagup = []
            y = j
            for i in range(6):
                if x < 0:
                    continue
                if y < 0:
                    continue
                try:
                    diagup.append(board2[x][y])
                    x -= 1
                    y += 1
                except:
                    pass
            diags.append(diagup)

    sequences.extend(copy.deepcopy(diags))


    for cells in sequences:
        matches = 1
        for i in range(len(cells)-1):
            symbol = cells.pop(0)
            if symbol is None:
                matches = 1
                continue
            elif cells[0] == symbol:
                matches += 1
                if matches == 4:
                    return True
            else:
                matches = 1
                continue

    return False


# game over, player is declared winner

def main():
    # create players, symbols, & decide who goes first
    players = ["Elliott", "Computer"]
    symbols = ["O", "@"]
    active_player_index = 0

    print("Let's play some Connect 4!")
    print("Today's players are: ", players)

    board = create_board()
    play_game(board, players, symbols, active_player_index)


if __name__ == '__main__':
    main()
