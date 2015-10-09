__author__ = 'porthunt'

from HTMLParser import HTMLParser

'''
Parses the website information.
'''

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
      if name == 'class' and value == 'TextBreak': #Name
        break
      elif name == 'id' and value == 'masterBody_trMaker': #Manufacturer
        break
      elif name == 'id' and value == 'masterBody_trScale': #Scale
        break
      elif name == 'id' and value == 'masterBody_trSerieshin': #Series
        break
      elif name == 'id' and value == 'masterBody_trSalseDate': #Release Date
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

  '''
  Parses the item information. Verifies if the
  item is a gunpla and formats the item info.
  '''

  def parse_gunpla(self, parser_data):
      preorder = False
      lst = list()
      for item in parser_data:
          item = item.replace('\r\n\t\t\t\t', '').strip()

          if item.strip() != '' and item.strip() != ':' and item.strip() != ',':
              lst.append(item)

      if 'Gundam Model Kits' not in lst[0]:
          raise ValueError('It is not a gundam model kit.')

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
