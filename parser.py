from HTMLParser import HTMLParser

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
