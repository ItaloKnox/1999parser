import re
import datetime

class Gunpla(object):
    def __init__(self, gunpla_id, lst):
        self.id = gunpla_id
        self.name = re.sub(r'\([^)]*\)', '', lst[0])
        self.manufacture = lst[1]
        self.scale = lst[2]
        self.series = lst[3]
        self.release_date = re.sub(r'^\W*\w+\W*', '', lst[4]).replace('.', '')
        self.release_date_code = datetime.datetime.strptime(
                                 self.release_date,
                                 '%b, %Y')

    def __str__(self):
        return ('ID: {} \nNAME: {} \nMANUFACTURE: {} \nSCALE: {} \n'
               'SERIES: {} \nRELEASE DATE: {}'.format(self.id, self.name,
               self.manufacture, self.scale, self.series, self.release_date))
