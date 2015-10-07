__author__ = 'porthunt'

from gunpla import Gunpla
from parser import LinksParser
import requests


def parse_gunpla():
    preorder = False
    lst = list()
    for item in parser.data:
        item = item.replace('\r\n\t\t\t\t', '').strip()

        if item.strip() != '' and item.strip() != ':' and item.strip() != ',':
            lst.append(item)

    if 'Pre-order' in lst[-1]:
        preorder = True

    gunpla = {'name':lst[0]}

    for idx,item in enumerate(lst):
        if lst[idx] == 'Manufacturer':
            gunpla['manufacture'] = lst[idx+1]
        elif lst[idx] == 'Scale':
            if lst[idx+2] == 'Original':
                gunpla['scale'] = lst[idx+1]
            else:
                gunpla['scale'] = lst[idx+2]
        elif lst[idx] == 'Original':
            gunpla['series'] = lst[idx+1]
        elif lst[idx] == 'Release Date':
            if not preorder:
                gunpla['release date'] = lst[idx+1]
            else:
                gunpla['release date'] = 'Pre-Order'
        else:
            pass

    gunpla['grade'] = ''
    grades = ['FG', 'SD', 'HG', 'MG', 'RG', 'PG', 'RE/100']

    for item in grades:
        if '('+item in gunpla['name']:
            gunpla['grade'] = item


    return gunpla

while(True):
    parser = LinksParser()
    link = 'http://www.1999.co.jp/eng/10011577'
    page = requests.get(link.strip())
    if page.status_code == 200:
        parser.feed(page.text)
        product = parse_gunpla()
        if not product:
            break
        gunpla_id = link.split('/')[-1]
        gunpla = Gunpla(gunpla_id, product)
        print(gunpla)
        break
