import copy

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

def print_board(board):
    print("\nHere is the board:")

    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=' | ')
        print()

def main():
    board = [['0', None, None, None, None, None, None], ['@', None, None, None, None, None, None],
             ['0', None, None, None, None, None, '@'], ['@', '0', None, None, None, '0', '0'],
             ['@', '@', '0', None, '0', '0', '@'], ['0', '0', '@', '0', '0', '@', '@']]
    winner = False

    print_board(board)
    winner = find_winner(board)

    if winner == True:
        print("Game Over!")
    else:
        print("Sorry :(")
if __name__ == '__main__':
    main()
