__author__ = 'porthunt'

from gunpla import Gunpla
from parser import LinksParser
import requests


def parse_gunpla(lst):
    for item in parser.data:
        item = item.replace('\r\n\t\t\t\t', '').strip()
        if item.strip() != '' and item.strip() != ':':
                lst.append(item)

    for idx,item in enumerate(lst):
        if idx % 2 != 0:
            lst[idx] = ''

    while '' in lst:
        lst.remove('')


while(True):
    parser = LinksParser()
    link = 'http://www.1999.co.jp/eng/10310668'
    page = requests.get(link)
    if page.status_code == 200:
        parser.feed(page.text)
        lst = list()
        parse_gunpla(lst)
        gunpla_id = link.split('/')[-1]
        gunpla = Gunpla(gunpla_id, lst)
        print(gunpla)
        break
