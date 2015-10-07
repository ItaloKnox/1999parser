__author__ = 'porthunt'

from gunpla import Gunpla
from parser import LinksParser
import requests

def run_one(url):
    while(True):
        parser = LinksParser()
        page = requests.get(url.strip())
        try:
            if page.status_code == 200:
                parser.feed(page.text)
                product = parser.parse_gunpla(parser.data)
                if not product:
                    break
                gunpla_id = url.split('/')[-1]
                gunpla = Gunpla(gunpla_id, product)
                break
        except ConnectionError:
            print('Connection aborted.')
            break
    return gunpla

def run_list(file_path, extension):
    url_list = open(file_path+extension, 'r')
    url_list_results = open(file_path+'_results'+extension, 'w')
    for item in url_list:
        gunpla = run_one(item)
        print(gunpla.summary())
        url_list_results.write(gunpla.summary())
        print('==================')
        url_list_results.write('\n==================\n')

user_choice = raw_input('Test [o]ne gunpla or a [l]ist? ')

if user_choice.lower() == 'o':
    url = raw_input('Type the URL: ')
    print(run_one(url))

elif user_choice.lower() == 'l':
    file_path = raw_input('File name: ')
    extension = raw_input('Extension: ')
    run_list(file_path, extension)
