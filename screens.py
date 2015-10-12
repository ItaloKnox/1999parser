__author__ = 'porthunt'


class Screens(object):

    def welcome_screen(self):
        print('')
        print('+'+'-'*71+'+')
        print('| Welcome to the 1999parser.'
              'Select the option you want to enter.\t|')
        print('|'+'\t'*9+'|')
        print('| [P]RODUCTION. The parser will start '
              'parsing the website from\t\t|\n'
              '| where it stopped the last time. (SERVER ONLY)\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('| [T]ESTING. It will ask for an URL '
              'or a file name (bulk test). \t|\n'
              '| If there is a mongoDB in your machine, '
              'the parser will add it.\t|')
        print('|'+'\t'*9+'|')
        print('| [A]NALYSIS. Shows information about'
              ' the database. (SERVER ONLY)'
              '\t|')
        print('|'+'\t'*9+'|')
        print('| [E]XIT.\t\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('+'+'-'*71+'+')
        print('')

    def production_screen(self):
        print('')
        print('+'+'-'*71+'+')
        print('| PRODUCTION MODE\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('| UNDER DEVELOPMENT. :(\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('| Type E to exit.\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('+'+'-'*71+'+')
        print('')

    def testing_screen(self):
        print('')
        print('+'+'-'*71+'+')
        print('| TESTING MODE\t\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('| [O]NE TEST. Type an URL and it will extract the info\t\t\t|\n'
              '| and insert on the database.\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('| [L]IST MODE. Fill a file with some URLs and it will \t\t\t|\n'
              '| insert them on the database.\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('| [E]XIT.\t\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('+'+'-'*71+'+')
        print('')

    def analysis_screen(self):
        print('')
        print('+'+'-'*71+'+')
        print('| ANALYSIS MODE\t\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('| UNDER DEVELOPMENT. :(\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('| Type E to exit.\t\t\t\t\t\t\t|')
        print('|'+'\t'*9+'|')
        print('+'+'-'*71+'+')
        print('')
