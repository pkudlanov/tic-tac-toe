# board = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'] # Original Board BAK
board = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

def player_marker_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O: ')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else: player2 = 'X'

    return (player1, player2)

def display_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print(f'---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print(f'---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

def place_marker(board, marker, position):
    board[position - 1] = marker.upper()

def win_check(baord, marker):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for positions_set in win_conditions:
        win_or_not = []
        for pos in positions_set:
            if(board[pos] == marker):
                win_or_not.append(marker)
        
        if(len(win_or_not) == 3):
            return True
        else: win_or_not = []
    
    return False


player1_marker, player2_marker = player_marker_input()

print(player1_marker, player2_marker)

display_board(board)


## Tests

# place_marker(board, player1_marker, 3)

# display_board(board)

# hello = win_check(board, 'X')
# print('RESULT OF FUNCTION', hello)

# Small Position Numbers for Reference
# ¹
# ²
# ³
# ⁴
# ⁵
# ⁶
# ⁷
# ⁸
# ⁹