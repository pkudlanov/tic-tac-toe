import random


def player_marker_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O: ').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def display_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print(f'---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print(f'---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def place_marker(board, marker, position):
    board[position] = marker.upper()


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
        else:
            win_or_not = []
    return False


def first_to_go():
    players = ['player1', 'player2']

    player_to_go = players[random.randint(0, 1)]
    print('r '.join(player_to_go.capitalize().split('r')) + ' will go first.')
    return player_to_go


def position_available(board, position):
    return board[position] != 'X' and board[position] != 'O'


def board_full_check(board):
    for char in board:
        if (char != 'X' and char != 'O'):
            return False
    return True


def replay_or_not():
    answer = ''

    while answer != 'y' and answer != 'n':
        answer = input("Would you like to play again? Press 'Y' or 'N'. >> ").lower()
    if answer == 'y':
        # board = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
        # board = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
        return True
    else:
        return False


def position_input(player):
    position = 0
    while not 1 <= position < 10:
        position = int(input(player + ' where will you go? >> '))

    return position - 1


game_in_session = True
players_turn = ''

print('Welcome to the wonderful classic of Tic Tac Toe!!!!')

while game_in_session:
    board = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

    player1_marker, player2_marker = player_marker_input()

    players_turn = first_to_go()

    print('Player markers: ' + player1_marker, player2_marker)

    display_board(board)
    while not board_full_check(board):
        if players_turn == 'player1':
            position = position_input('Player 1')
            # print(position_available(board, position))
            while not position_available(board, position):
                print('That position is not available.')
                position = position_input('Player 1')
            place_marker(board, player1_marker, position)
            display_board(board)
            if win_check(board, player1_marker):
                print('Congratulations Player 1 won!!')
                break
            elif board_full_check(board):
                print('It\'s a draw.')
                break
            players_turn = 'player2'
        elif players_turn == 'player2':
            position = position_input('Player 2')
            # print(position_available(board, position))
            while not position_available(board, position):
                print('That position is not available.')
                position = position_input('Player 2')
            place_marker(board, player2_marker, position)
            display_board(board)
            if win_check(board, player2_marker):
                print('Congratulations Player 2 won!!')
                break
            elif board_full_check(board):
                print('It\'s a draw.')
                break
            players_turn = 'player1'

    game_in_session = replay_or_not()
