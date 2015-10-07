__author__ = 'porthunt'

from gunpla import Gunpla
#from parser import LinksParser
from HTMLParser import HTMLParser
import requests

class LinksParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.data = []

  def handle_starttag(self, tag, attributes):
    if tag != 'div' and tag !='tr':
      return
    if self.recording:
      self.recording += 1
      return
    for name, value in attributes:
      if name == 'class' and value == 'TextBreak':
        break
      elif name == 'id' and value == 'masterBody_trMaker':
        break
      elif name == 'id' and value == 'masterBody_trScale':
        break
      elif name == 'id' and value == 'masterBody_trSerieshin':
        break
      elif name == 'id' and value == 'masterBody_trSalseDate':
        break
    else:
      return
    self.recording = 1

  def handle_endtag(self, tag):
    if tag == 'div' and self.recording:
      self.recording -= 1
    elif tag == 'tr' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)

  def parse_gunpla(self, parser_data):
      preorder = False
      lst = list()
      for item in parser_data:
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

def run_one(url):
    gunpla = None
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
        except requests.ConnectionError:
            print('Connection aborted.')
            break
    return gunpla

def run_list(file_path, extension):
    url_list = open(file_path+extension, 'r')
    url_list_results = open(file_path+'_results'+extension, 'w')
    for item in url_list:
        gunpla = run_one(item)
        try:
            print(gunpla.summary())
            url_list_results.write(gunpla.summary())
            print('==================')
            url_list_results.write('\n==================\n')
        except:
            print('fuck')

user_choice = raw_input('Test [o]ne gunpla or a [l]ist? ')

if user_choice.lower() == 'o':
    url = raw_input('Type the URL: ')
    print(run_one(url))

elif user_choice.lower() == 'l':
    file_path = raw_input('File name: ')
    extension = raw_input('Extension: ')
    run_list(file_path, extension)
