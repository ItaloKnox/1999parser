__author__ = 'porthunt'

from parser import LinksParser
from screens import Screens

############
#   MAIN   #
############

screens = Screens()

while True:
    screens.welcome_screen()
    user_input = raw_input('Select your option: ')

    #Production
    if user_input.upper() == 'P':
        while True:
            screens.production_screen()
            user_input = raw_input('Select your option: ')

            if user_input.upper() == 'E':
                break

    #Testing
    elif user_input.upper() == 'T':
        parser = LinksParser()
        while True:
            screens.testing_screen()
            user_input = raw_input('Select your option: ')

            #One Test
            if user_input.upper() == 'O':
                url = raw_input('Type the URL: ')
                gunpla = parser.run_one(url)

            #Bulk Test
            elif user_input.upper() == 'L':
                file_path = raw_input('File name: ')
                extension = raw_input('Extension: ')
                if extension[0] != '.':
                    extension = '.'+extension
                parser.run_list(file_path, extension)

            #Exit
            elif user_input.upper() == 'E':
                break

    #Analysis
    elif user_input.upper() == 'A':
        while True:
            screens.analysis_screen()
            user_input = raw_input('Select your option: ')

            if user_input.upper() == 'E':
                break

    #Exit
    elif user_input.upper() == 'E':
        print('Bye!')
        exit()

    else:
        print('\nNot a valid option. Try again.')

'''


elif user_choice.lower() == 'l':
    file_path = raw_input('File name: ')
    extension = raw_input('Extension: ')
    if extension[0] != '.':
        extension = '.'+extension
    parser.run_list(file_path, extension)
'''
