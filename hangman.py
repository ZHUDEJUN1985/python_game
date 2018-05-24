import random

HANGMAN_PICTURE = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
+---+
O   |
|   |
    |
   ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/  \ |
    ===''', '''
 +---+
[O   |
/|\  |
/ \  |
    ===''', '''
 +---+
[O]  |
/|\  |
/ \  |
    ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar deer dog eagle fox frog lion snake'.split()

words_dict = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
              'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron'.split(),
              'Fruits': 'apple orange lemon pear cherry banana mango strawberry tomato lime'.split(),
              'Animals': 'bat bear cat deer dog duck eagle fish frog lion monkey tiger panda'.split()}


def get_random_word(word_list):
    word_id = random.randint(0, len(word_list) - 1)
    return word_list[word_id]


def get_random_word_from_dict(word_dict):
    word_key = random.choice(list(word_dict.keys()))
    word_id = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_id], word_key]


def display(wrong_letters, correct_letters, secret_word):
    print(HANGMAN_PICTURE[len(wrong_letters)])
    print()

    print('Wrong letters:', end='')
    for i in wrong_letters:
        print(i, end='')
    print()

    blanks = '_ ' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i * 2] + secret_word[i] + blanks[i * 2 + 1:]

    print(blanks)
    print()


def get_guess(has_guessed_letters):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in has_guessed_letters:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def play_again():
    print('Do you want to play again?(yes or no)')
    play = input()
    return play.lower().startswith('y')


def game1():
    print('H A N G M A N')
    wrong_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)
    game_is_over = False

    while True:
        display(wrong_letters, correct_letters, secret_word)

        guess = get_guess(wrong_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break

            if found_all_letters:
                print('YES! The secret word is "' + secret_word + '"! You have won!')
                game_is_over = True
        else:
            wrong_letters = wrong_letters + guess

            if len(wrong_letters) == len(HANGMAN_PICTURE) - 1:
                display(wrong_letters, correct_letters, secret_word)

                print('You have run out of guesses!\n After ' + str(len(wrong_letters)) + ' wrong guesses and '
                      + str(len(correct_letters)) + ' correct guesses, the secret word is "' + secret_word + '".')
                game_is_over = True

        if game_is_over:
            if play_again():
                wrong_letters = ''
                correct_letters = ''
                secret_word = get_random_word(words)
                game_is_over = False
            else:
                break


def game2():
    print('H A N G M A N')
    difficulty = ''
    while difficulty not in ['E', 'M', 'H']:
        print('Please choose difficulty: E-Easy, M-Medium, H-Hard')
        difficulty = input()
        difficulty = difficulty.upper()

    if difficulty == 'M':
        del HANGMAN_PICTURE[8]
        del HANGMAN_PICTURE[7]
    if difficulty == 'H':
        del HANGMAN_PICTURE[8]
        del HANGMAN_PICTURE[7]
        del HANGMAN_PICTURE[5]
        del HANGMAN_PICTURE[3]

    wrong_letters = ''
    correct_letters = ''
    secret_word, secret_set = get_random_word_from_dict(words_dict)
    game_is_over = False

    while True:
        display(wrong_letters, correct_letters, secret_word)

        guess = get_guess(wrong_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break

            if found_all_letters:
                print('YES! The secret word is "' + secret_word + '", and it belongs the set "'
                      + secret_set + '". You have won!')
                game_is_over = True
        else:
            wrong_letters = wrong_letters + guess

            if len(wrong_letters) == len(HANGMAN_PICTURE) - 1:
                display(wrong_letters, correct_letters, secret_word)

                print('You have run out of guesses!\n After ' + str(len(wrong_letters)) + ' wrong guesses and '
                      + str(len(correct_letters)) + ' correct guesses, the secret word is "' + secret_word + '".')
                game_is_over = True

        if game_is_over:
            if play_again():
                wrong_letters = ''
                correct_letters = ''
                secret_word, secret_set = get_random_word_from_dict(words_dict)
                game_is_over = False
            else:
                break


def main():
    # game1()
    game2()


if __name__ == '__main__':
    main()
