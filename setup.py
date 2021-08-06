from os import path
from datetime import datetime
import json
from auth.hash import hash_text


def main():
    print('''
INSTRUCTIONS:
  1. The stream name is what you want the stream to be called. For instance, auditorium_feed.
  2. The stream password is what you'll use to authenticate with the server. There's no way to recover this, so make sure you write it down!
    ''')

    while True:
        stream_name = str(input('Stream Name: '))
        stream_key = str(input('Stream Password: '))

        print(f'\nYour stream credentials:\n  Name: {stream_name}\n  Password: {stream_key}')
        response = str(input('\nIs this information correct? (Y/N): '))

        if response.upper() == 'Y':
            dict = {'stream_name': stream_name, 'stream_key': hash_text(stream_key), 'live': False}

            with open(path.join(path.curdir, 'auth', 'stream_keys', f'{stream_name}.json'), 'w') as j:
                json.dump(dict, j)

            cont = input('Configuration saved. Add another? (Y/N): ')
  
            if str(cont).upper() == 'N':
                break
            else:
                continue
        else:
            continue


if __name__ == '__main__':
    main()