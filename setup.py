from os import path, mkdir
import json
from typing import Type
from auth.hash import hash_text


def text_input(prompt):
    text_string = str(input(f'{prompt}'))
    for letter in str(text_string):
        if not letter.isalpha() and not letter.isnumeric():
            raise TypeError('ERROR: You can only use letters and numbers in your stream name and password.')
    return text_string


def check_dir(dir):
    if not path.exists(dir):
        mkdir(dir)


def main():

    print('''
INSTRUCTIONS:
  1. The stream name is what you want the stream to be called. For instance, auditorium_feed. Only use letters, numbers, and - or _ in the name.
  2. The stream password is what you'll use to authenticate with the server. There's no way to recover this, so make sure you write it down!
    ''')

    while True:
        try:
            stream_name = text_input(prompt='Stream Name: ')
        except Exception as error:
            print(error)
            continue

        try:
            stream_password = hash_text(text_input(prompt='Stream Password: '))
        except Exception as error:
            print(error)
            continue

        dict = {'stream_name': stream_name, 'stream_key': stream_password, 'live': False}

        key_folder = path.join(path.curdir, 'auth', 'stream_keys')
        check_dir(key_folder)

        with open(path.join(key_folder, f'{stream_name}.json'), 'w') as j:
            json.dump(dict, j)

        response = input('Configuration saved. Add another? (Y/N): ')
        if str(response).upper() == 'N':
            break
        else:
            continue


if __name__ == '__main__':
    main()