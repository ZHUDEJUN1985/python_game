import random

NUM_DIGITS = 3
MAX_GUESS = 10


def get_secret_number():
    number_list = list(range(0, 10))
    random.shuffle(number_list)

    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(number_list[i])

    return secret_num


def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'

    clue = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clue.append('Fermi')
        elif guess[i] in secret_num:
            clue.append('Pico')

    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)


def is_all_digits(num):
    if num == '':
        return False
    for i in num:
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False

    return True


def main():
    print('Welcome to Bagels!')
    print('I am thinking of a %s-digit number. Try to guess what is it!' % NUM_DIGITS)
    print('The clues I give are...')
    print('When I say:       That means:')
    print('Bagels            None of the digits is correct.')
    print('Pico              One digit is correct but in the wrong position.')
    print('Fermi             One digit is correct and in the right position.')

    while True:
        secret_number = get_secret_number()
        print('I have thought up a number. You have %s guesses to get it.' % MAX_GUESS)

        count = 1
        while count <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_DIGITS or not is_all_digits(guess):
                print('Guess #%d:   ' % count)
                guess = input()

            print(get_clues(guess, secret_number))
            count += 1

            if guess == secret_number:
                break
            if count > MAX_GUESS:
                print('You ran out of guesses. The answer was %s.' % secret_number)

        print('Do you want to play again?(yes or no)')
        play = input()
        if not play.lower().startswith('y'):
            break


if __name__ == '__main__':
    main()
