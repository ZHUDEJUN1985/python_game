import random
import sys


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)


def get_mode():
    while True:
        print('Do you wish to encrypt or decrypt the message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Please enter either "encrypt", "e", "decrypt", "d".')


def get_message():
    print('Please enter your mseeage:')
    return input()


def get_key():
    while True:
        print('Please enter the key between 1-%d.' % MAX_KEY_SIZE)
        key = int(input())
        if 1 <= key <= MAX_KEY_SIZE:
            return key
        else:
            print('Attention! The number should between 1-%d,' % MAX_KEY_SIZE)


def get_translate_message(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for s in message:
        s_id = SYMBOLS.find(s)
        if s_id == -1:
            translated += s
        else:
            s_id += key
            if s_id >= MAX_KEY_SIZE:
                s_id -= MAX_KEY_SIZE
            elif s_id < 0:
                s_id += MAX_KEY_SIZE

            translated += SYMBOLS[s_id]

    return translated


def main():
    print('Begin to encrypt or decrypt the message.')
    mode = get_mode()
    msg = get_message()
    key = get_key()
    res = get_translate_message(mode, msg, key)
    print('Your translated text is:')
    print(res)


if __name__ == '__main__':
    main()
