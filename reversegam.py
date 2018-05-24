import random
import sys

WIDTH = 8
HEIGHT = 8
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8']


def draw_board(board):
    digit_line = '   1 2 3 4 5 6 7 8'
    corner_line = '+- - - - - - - - - -+'

    print(digit_line)
    print(corner_line)
    for i in range(8):
        print('%d| ' % (i+1), end='')
        for j in range(8):
            print('%s ' % board[i][j], end='')
        print('|%d' % (i+1))
    print(corner_line)
    print(digit_line)


def get_new_board():
    board = []
    for i in range(8):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

    return board


def is_on_board(x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        return True
    else:
        return False


def is_valid_move(board, flag, x_start, y_start):
    if board[x_start][y_start] != ' ' or not is_on_board(x_start, y_start):
        return False

    if flag == 'X':
        other_flag = 'O'
    else:
        other_flag = 'X'

    directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    find_flip = []
    for x_, y_ in directions:
        x, y = x_start, y_start
        x += x_
        y += y_
        while is_on_board(x, y) and board[x][y] == other_flag:
            x += x_
            y += y_
            if is_on_board(x, y) and board[x][y] == flag:
                while True:
                    x -= x_
                    y -= y_
                    if x == x_start and y == y_start:
                        break
                    find_flip.append([x, y])

    if len(find_flip) == 0:
        return False

    return find_flip


def get_valid_move(board, flag):
    valid_moves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_valid_move(board, flag, x, y):
                valid_moves.append([x, y])

    return valid_moves


def get_board_copy(board):
    copy_board = get_new_board()
    for i in range(WIDTH):
        for j in range(HEIGHT):
            copy_board[i][j] = board[i][j]

    return copy_board


def get_board_valid_move(board, flag):
    copy_board = get_board_copy(board)
    for x, y in get_valid_move(board, flag):
        copy_board[x][y] = '.'

    return copy_board


def get_score(board):
    x_score, o_score = 0, 0
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if board[i][j] == 'X':
                x_score += 1
            if board[i][j] == 'O':
                o_score += 1

    return {'X': x_score, 'O':o_score}


def get_player_flag():
    flag = ''
    while flag != 'X' and flag != 'O':
        print('Do you want to be X or O?')
        flag = input().upper()

    if flag == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'player'
    else:
        return 'computer'


def move(board, flag, x_start, y_start):
    flag_to_flip = is_valid_move(board, flag, x_start, y_start)
    if not flag_to_flip:
        return False

    board[x_start][y_start] = flag
    for x, y in flag_to_flip:
        board[x][y] = flag

    return True


def is_on_corner(x, y):
    return (x == 0 or x == (WIDTH - 1)) and (y == 0 or y == (HEIGHT - 1))


def player_move(board, player_flag):
    while True:
        print('Please enter your move, or "quit", or"hints."')
        p_move = input()

        if p_move == 'quit' or p_move == 'hints':
            return p_move

        if len(p_move) == 2 and p_move[0] in DIGITS and p_move[1] in DIGITS:
            x, y = int(p_move[0]) - 1, int(p_move[1]) - 1
            if not is_valid_move(board, player_flag, x, y):
                continue
            else:
                break
        else:
            print('That is not a valid move. Please enter column (1-8) and then row(1-8)')
            print('For example, 81 will move on the top-right corner.')

    return [x, y]


def computer_move(board, computer_flag):
    candidates_move = get_valid_move(board, computer_flag)
    if not candidates_move:
        random.shuffle(candidates_move)

    for x, y in candidates_move:
        if is_on_corner(x, y):
            return [x, y]

    best_score = -1
    best_move = [0, 0]
    for x, y in candidates_move:
        copy_board = get_board_copy(board)
        move(copy_board, computer_flag, x, y)
        score = get_score(copy_board)
        if score[computer_flag] > best_score:
            best_move = [x, y]
            best_score = score[computer_flag]

    return best_move


def print_score(board, player_flag, computer_flag):
    score = get_score(board)
    print('You: %d points. Computer: %d points.' % (score[player_flag], score[computer_flag]))


def play_game(player_flag, computer_flag):
    show_hints = False
    turn = who_goes_first()
    print('The %s will goes first.' % turn)

    board = get_new_board()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        player_candidates = get_valid_move(board, player_flag)
        computer_candidates = get_valid_move(board, computer_flag)

        if player_candidates == [] and computer_candidates == []:
            return board
        elif turn == 'player':
            if player_candidates:
                if show_hints:
                    valid_move_board = get_board_valid_move(board, player_flag)
                    draw_board(valid_move_board)
                else:
                    draw_board(board)

                print_score(board, player_flag, computer_flag)
                p_move = player_move(board, player_flag)
                if p_move == 'quit':
                    print('Thanks for playing.')
                    sys.exit()
                elif p_move == 'hints':
                    show_hints = not show_hints
                    continue
                else:
                    move(board, player_flag, int(p_move[0]), int(p_move[1]))
            turn = 'computer'
        elif turn == 'computer':
            if computer_candidates:
                draw_board(board)
                print_score(board, player_flag, computer_flag)
                input('Please enter to see the computer\'s move.')
                c_move = computer_move(board, computer_flag)
                move(board, computer_flag, int(c_move[0]), int(c_move[1]))
            turn = 'player'


def main():
    print('Welcome to Reversegam!')
    player_flag, computer_flag = get_player_flag()

    while True:
        final_board = play_game(player_flag, computer_flag)
        draw_board(final_board)
        score = get_score(final_board)

        print('X scored %d points, O scored %d points.' % (score['X'], score['O']))

        if score[player_flag] > score[computer_flag]:
            print('You beat the computer by %d points! Congratulations!' % (score[player_flag] - score[computer_flag]))
        elif score[player_flag] < score[computer_flag]:
            print('You lost. The computer beat you by %d points.' % (score[computer_flag] - score[player_flag]))
        else:
            print('The game was a tie!')

        print('Do you want to play again?(yes or no)')
        user_input = input().lower()
        if not user_input.startswith('y'):
            break


if __name__ == '__main__':
    main()
