import random
import sys
import math


def get_new_board():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')

    return board


def draw_board(board):
    top_line = '   '
    for i in range(1, 6):
        top_line += ' ' * 9 + str(i)
    print(top_line)
    print('  ' + '0123456789' * 6)

    for row in range(15):
        first_space = ''
        if row < 10:
            first_space = ' '

        board_row = ''
        for col in range(60):
            board_row += board[col][row]
        print(first_space + str(row) + board_row + str(row))

    print('  ' + '0123456789' * 6)
    print(top_line)


def get_random_chests(num_chests):
    chests = []
    while len(chests) < num_chests:
        chest = [random.randint(0, 59), random.randint(0, 14)]
        if chest not in chests:
            chests.append(chest)

    return chests


def is_on_board(x, y):
    return 0 <= x < 60 and 0 <= y < 15


def move(board, chests, x, y):
    smallest_distance = 100
    for cx, cy in chests:
        dist = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        if dist < smallest_distance:
            smallest_distance = dist

    smallest_distance = round(smallest_distance)
    if smallest_distance == 0:
        chests.remove([x, y])
        return 'You have found a sunken treasure chest.'
    else:
        if smallest_distance < 10:
            board[x][y] = str(smallest_distance)
            return 'Treasure detected at a distance of %d from the sonar device' % smallest_distance
        else:
            board[x][y] = 'X'
            return 'Sonar did not detect anything. All treasure chests out of range.'


def get_player_move(has_moved):
    print('Where do you want to drop the next sonar device? (0-59  0-14) or type quit')
    while True:
        pos = input()
        if pos.lower() == 'quit':
            print('Thanks for playing.')
            sys.exit()

        pos = pos.split()
        if not is_on_board(int(pos[0]), int(pos[1])):
            print('Please enter a number from 0 to 59, a space, then a number from 0 to 14.')
            continue

        if len(pos) == 2 and pos[0].isdigit() and pos[1].isdigit():
            if [int(pos[0]), int(pos[1])] in has_moved:
                print('You already moved there.')
                continue
            return [int(pos[0]), int(pos[1])]


def show_instructions():
    print('''Instructions:
    You are the captain of the Simon, a treasure-hunting ship. Your current mission is to
    use sonar devices to find three sunken treasure chests at the bottom of the ocean.
    But you only have cheap sonar that finds distance, not direction.
    Enter the coordinates to drop a sonar device. The ocean map will be marked with how far
    away the nearest chest is, or an X if it is beyond the sonar device's range.
    For example, the C marks are where chests are. The sonar device shows a 3 because the
    closest chest is 3 spaces away.
    
                      1         2         3
            0123456789012345678901234567890123456789
           0~~~~`~```~`~``~~~```~~~`~``~~```~`~```~~0
           1~~```~``~``~~```~~~~````~~`~``````~~~`~`1
           2`~`C``3`~~~``C`~~~~````~~~~`~~``~~~~`~~`2
           3````~~~~`~~~`~~```~~~````~~~``~```~~`~~`3
           4~`~~~~``~~```C``~~~```~~~```~~~~````~`~~4
            0123456789012345678901234567890123456789
                      1         2         3          
    (In the real game, the chests are not visible in the ocean.)
    
    Press enter to continue...''')
    input()

    print('''When you drop a sonar device directly on a chest, you retrieve it and the 
    other sonar devices update to show how far away the next nearest chest is.
    The chests are beyond the range of the sonar device on the left, so it shows an X.
    
                      1         2         3
            0123456789012345678901234567890123456789
           0~~~~`~```~`~``~~~```~~~`~``~~```~`~```~~0
           1~~```~``~``~~```~~~~````~~`~``````~~~`~`1
           2`~`X``7`~~~``C`~~~~````~~~~`~~``~~~~`~~`2
           3````~~~~`~~~`~~```~~~````~~~``~```~~`~~`3
           4~`~~~~``~~```C``~~~```~~~```~~~~````~`~~4
            0123456789012345678901234567890123456789
                      1         2         3          
    
    The treasure chests don't move around.Sonar devices can detect treasure chests up to
     a distance of 9 spaces. Try to collcet all 3 chests before running out of sonar devices.
     Good luck!
     
     Press enter to continue...''')
    input()


def main():
    print('S O N A R!')
    print()
    print('Would you like to view the instructions?(yes or no)')
    player_choice = input()
    if player_choice.lower().startswith('y'):
        show_instructions()

    while True:
        sonar_devices = 20
        the_board = get_new_board()
        the_chests = get_random_chests(3)
        draw_board(the_board)
        has_moved = []

        while sonar_devices > 0:
            print('You have %d sonar devices left. %d treasure chests remaining.' % (sonar_devices, len(the_chests)))
            x, y = get_player_move(has_moved)
            has_moved.append([x, y])

            result_msg = move(the_board, the_chests, x, y)
            if result_msg == 'You have found a sunken treasure chest.':
                for x_, y_ in has_moved:
                    move(the_board, the_chests, x_, y_)

            draw_board(the_board)
            print(result_msg)

            if len(the_chests) == 0:
                print('You have found all the sunken treasure chests! Congratulations and good game!')
                break

            sonar_devices -= 1

        if sonar_devices == 0:
            print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
            print('for home with treasure chests still out there! Game over.')
            print('The remaining chests were here:')
            for x, y in the_chests:
                print('%d, %d' % (x, y))

            print('Do you want to play again?(yes or no)')
            player_choice = input()
            if not player_choice.lower().startswith('y'):
                sys.exit()


if __name__ == '__main__':
    main()
