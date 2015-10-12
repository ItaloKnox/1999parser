from parser import LinksParser
from screens import Screens
import datetime

__author__ = 'porthunt'

# Main

screens = Screens()

screens.welcome_screen()
while True:
    user_input = raw_input('Select your option ([P], [T], [A], [E]): ')

    # Production
    if user_input.upper() == 'P':
        screens.production_screen()
        while True:
            user_input = raw_input('Select your option ([E]): ')

            # Exit
            if user_input.upper() == 'E':
                break

            if user_input.upper() == 'R':
                parser = LinksParser()
                fmt = '%Y-%m-%d %H:%M:%S'
                now = datetime.datetime.now()
                print('Started at {}'.format(now.strftime(fmt)))
                for _ in range(10350000, 10350200):
                    url = 'http://www.1999.co.jp/eng/{}'.format(_)
                    print(url)
                    gunpla = parser.run_one(url)
                end = datetime.datetime.now()
                print('Ended at {}'.format(end.strftime(fmt)))
                diff = end - now
                print('Process executed in {} seconds.'
                      .format(diff.total_seconds()))
                break

    # Testing
    elif user_input.upper() == 'T':
        parser = LinksParser()
        screens.testing_screen()
        while True:
            user_input = raw_input('Select your option ([O], [L], [E]): ')

            # One Test
            if user_input.upper() == 'O':
                url = raw_input('Type the URL: ')
                gunpla = parser.run_one(url)

            # Bulk Test
            elif user_input.upper() == 'L':
                file_path = raw_input('File name: ')
                extension = raw_input('Extension: ')
                if extension[0] != '.':
                    extension = '.'+extension
                parser.run_list(file_path, extension)

            # Exit
            elif user_input.upper() == 'E':
                break

    # Analysis
    elif user_input.upper() == 'A':
        screens.analysis_screen()
        while True:
            user_input = raw_input('Select your option ([E]): ')

            if user_input.upper() == 'E':
                break

    # Exit
    elif user_input.upper() == 'E':
        print('Bye!')
        exit()

    else:
        print('\nNot a valid option. Try again.')
