__author__ = 'porthunt'

from gunpla import Gunpla
from parser import LinksParser
import requests
import re

parser = LinksParser()
page = requests.get('http://www.1999.co.jp/eng/10310668')
parser.feed(page.text)
gunpla = Gunpla(parser.data)
print(re.sub(r'\([^)]*\)', '', gunpla.name[1]))
