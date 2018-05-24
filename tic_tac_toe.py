import random


def draw_game_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def first_player():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def move(board, letter, pos):
    board[pos] = letter


def is_winner(board, letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) or \
           (board[4] == letter and board[5] == letter and board[6] == letter) or \
           (board[1] == letter and board[2] == letter and board[3] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[3] == letter and board[6] == letter and board[9] == letter) or \
           (board[1] == letter and board[5] == letter and board[9] == letter) or \
           (board[3] == letter and board[5] == letter and board[7] == letter)


def get_copy_of_board(board):
    copy_board = []
    for i in board:
        copy_board.append(i)
    return copy_board


def is_space_free(board, pos):
    return board[pos] == ' '


def choose_random_move(board, pos_list):
    candidate_move = []
    for i in pos_list:
        if is_space_free(board, i):
            candidate_move.append(i)

    if len(candidate_move) > 0:
        return random.choice(candidate_move)
    else:
        return None


def player_move(board):
    pos = ''
    while pos not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or not is_space_free(board, int(pos)):
        print('What is your next move? (1-9)')
        pos = input()

    return int(pos)


def computer_move(board, c_letter):
    if c_letter == 'X':
        p_letter = 'O'
    else:
        p_letter = 'X'

    for i in range(1, 10):
        temp_board = get_copy_of_board(board)
        if is_space_free(temp_board, i):
            move(temp_board, c_letter, i)
            if is_winner(temp_board, c_letter):
                return i

    for j in range(1, 10):
        temp_board = get_copy_of_board(board)
        if is_space_free(temp_board, j):
            move(temp_board, p_letter, j)
            if is_winner(temp_board, p_letter):
                return j

    pos = choose_random_move(board, [1, 3, 5, 7])
    if pos is not None:
        return pos

    if is_space_free(board, 5):
        return 5

    pos = choose_random_move(board, [2, 4, 6, 8])
    if pos is not None:
        return pos


def is_board_full(board):
    full_flag = True
    for i in board[1:]:
        if i == ' ':
            full_flag = False
            break

    return full_flag


def main():
    print('Welcome to Tic-Tac-Toe!')
    while True:
        board = [' '] * 10
        p_letter, c_letter = input_player_letter()
        turn = first_player()
        print('The' + turn + 'will go first.')
        game_over = False

        while not game_over:
            if turn == 'player':
                draw_game_board(board)
                pos = player_move(board)
                move(board, p_letter, pos)

                if is_winner(board, p_letter):
                    draw_game_board(board)
                    print('Wahoo! You have won the game!')
                    game_over = True
                else:
                    if is_board_full(board):
                        draw_game_board(board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                pos = computer_move(board, c_letter)
                move(board, c_letter, pos)

                if is_winner(board, c_letter):
                    draw_game_board(board)
                    print('The computer has beaten you! You lose.')
                    game_over = True
                else:
                    if is_board_full(board):
                        draw_game_board(board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

        print('Do you want to play again? (yes or no)')
        play_sign = input()
        if not play_sign.lower().startswith('y'):
            break


if __name__ == '__main__':
    main()
