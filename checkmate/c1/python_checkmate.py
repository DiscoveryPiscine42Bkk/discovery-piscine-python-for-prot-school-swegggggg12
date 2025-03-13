def is_king_in_check(board, king_position):
    for row_index, row in enumerate(board):
        for col_index, piece in enumerate(row):
            if piece != '.' and piece != 'K':  
                if can_capture(board, piece, (row_index, col_index), king_position):
                    return True
    return False

def can_capture(board, piece, piece_position, target_position):
    piece_row, piece_col = piece_position
    target_row, target_col = target_position

    if piece == 'P': 
        if abs(piece_col - target_col) == 1 and target_row - piece_row == 1:  
            return True
        if abs(piece_col - target_col) == 1 and piece_row - target_row == 1:  
            return True
    elif piece == 'B':  
        if abs(piece_row - target_row) == abs(piece_col - target_col):
            return is_path_clear(board, piece_position, target_position)
        elif piece == 'R':  
          if piece_row == target_row or piece_col == target_col:
            return is_path_clear(board, piece_position, target_position)
    elif piece == 'Q':  
        if (piece_row == target_row or piece_col == target_col) or \
           (abs(piece_row - target_row) == abs(piece_col - target_col)):
            return is_path_clear(board, piece_position, target_position)
    return False

def is_path_clear(board, start, end):
    step_row = 0 if start[0] == end[0] else (1 if end[0] > start[0] else -1)
    step_col = 0 if start[1] == end[1] else (1 if end[1] > start[1] else -1)
    current_row, current_col = start[0] + step_row, start[1] + step_col

    while (current_row, current_col) != end:
        if board[current_row][current_col] != '.':
            return False
        current_row += step_row
        current_col += step_col
    return True

def is_checkmate(board, king_position):
    if not is_king_in_check(board, king_position):
        return False

    king_row, king_col = king_position
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for move in moves:
        new_row = king_row + move[0]
        new_col = king_col + move[1]
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            board[king_row][king_col] = '.'
            board[new_row][new_col] = 'K'
            if not is_king_in_check(board, (new_row, new_col)):
                board[new_row][new_col] = '.'
                board[king_row][king_col] = 'K'
                return False
            board[new_row][new_col] = '.'
            board[king_row][king_col] = 'K'

    return True

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def main():
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', 'k']
    ]                                     
    print("Initial Board:")
    print_board(board)

    king_position = (7,4 )
    if is_checkmate(board, king_position):
        print("Checkmate! The king is in checkmate.")
    else:
        if is_king_in_check(board, king_position):
            print("The king is in check.")
        else:
            print("The king is safe.")

if __name__ == "__main__":
    main()