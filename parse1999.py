__author__ = 'porthunt'

from gunpla import Gunpla
from parser import LinksParser
import requests

'''
Returns the item of the given URL.
'''

def run_one(url):
    gunpla = None
    while(True):
        parser = LinksParser()
        page = requests.get(url.strip())
        try:
            if page.status_code == 200:
                parser.feed(page.text)

                if not parser.data: # check if it parsed nothing
                    break

                try:
                    product = parser.parse_gunpla(parser.data)
                except ValueError:
                    print('{} is not a gunpla model.'.
                          format(url.split('/')[-1]))
                    return None

                if not product:
                    break

                gunpla_id = url.split('/')[-1]
                gunpla = Gunpla(gunpla_id, product)
                gunpla.insert()
                break
        except requests.ConnectionError:
            print('Connection aborted.')
            break
    return gunpla

'''
Runs a list of URLs inside a file.
'''

def run_list(file_path, extension):
    url_list = open(file_path+extension, 'r')
    url_list_results = open(file_path+'_results'+extension, 'w')
    for item in url_list:
        gunpla = run_one(item)
        print(gunpla.summary())
        url_list_results.write(gunpla.summary())
        print('==================')
        url_list_results.write('\n==================\n')

######
#MAIN#
######

user_choice = raw_input('Test [o]ne gunpla or a [l]ist? ')

if user_choice.lower() == 'o':
     url = raw_input('Type the URL: ')
     gunpla = run_one(url)

elif user_choice.lower() == 'l':
    file_path = raw_input('File name: ')
    extension = raw_input('Extension: ')
    if extension[0] != '.':
        extension = '.'+extension
    run_list(file_path, extension)
