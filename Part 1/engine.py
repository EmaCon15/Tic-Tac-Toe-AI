BOARD_WIDTH = 3
BOARD_HEIGHT = 3

#1. Representing the board
def new_board():
    board = []
    for x in range(0, BOARD_WIDTH):
        row = []
        for y in range(0, BOARD_HEIGHT):
            row.append(None)
        board.append(row)
    return board

board = new_board()

#2. Print the board
def render(board):
    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)
    
    row_num = 0
    print ('  0 1 2 ')
    print ('  ------')
    for row in rows:
        output_row = ""
        for x in row:
            if x is None:
                output_row += " "
            else:
                output_row += x
        print("%d|%s|" % (row_num, ' '.join(output_row)))
        row_num+=1
    print ('  ------')

render(board)

#3. Execute moves
def make_move(player, board, move_coordinates):
    if board[move_coordinates[0]][move_coordinates[1]] is not None:
        raise Exception("Illegal move!")

    board[move_coordinates[0]][move_coordinates[1]] = player

#4. Check win condition
def get_winner(board):
    all_line_co_ords = get_all_line_co_ords()

    for line in all_line_co_ords:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]

    return None

def get_all_line_co_ords():
    cols = []
    for x in range(0, BOARD_WIDTH):
        col = []
        for y in range(0, BOARD_HEIGHT):
            col.append((x, y))
        cols.append(col)
        
#5. Check draw condition
def is_board_full(board):
    for col in board:
        for sq in col:
            if sq is None:
                return False
    return True

# Play
def play(player1_f, player2_f):
    players = [
        ('X', player1_f),
        ('O', player2_f),
    ]

    turn_number = 0
    board = new_board()
    while True:
        current_player_id, current_player_f = players[turn_number % 2]
        render(board)

        move_co_ords = current_player_f(board, current_player_id)
        make_move(current_player_id, board, move_co_ords)

        winner = get_winner(board)
        if winner is not None:
            render(board)
            print ("THE WINNER IS %s!" % winner)
            break

        if is_board_full(board):
            render(board)
            print ("IT'S A DRAW!")
            break

        turn_number += 1