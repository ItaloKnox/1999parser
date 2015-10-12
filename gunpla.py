import datetime
from gunpla_dao import GunplaDAO
import pytz
import re

__author__ = 'porthunt'

'''
Class that represents the gunpla.
- id: URL from the 1999.co.jp website
- (e.g. http://www.1999.co.jp/eng/10310668).
- name: item's name without the parenthesis text.
- manufacture: manufacturer of the item.
- grade: FG, SD, HG, MG, RG, PG, RE/100
- scale: gunpla's scale. Could be 1/144, 1/100, 1/60, no scale, etc.
- series: That gunpla's anime.
- release date: When it was released. Format: %b, %Y (e.g. Apr, 2015).
- release date code (Date format): Date format of 'release date' variable.
'''


class Gunpla(object):

    '''
    Creates the gunpla object. Mandatory fields: id and name.
    '''

    def __init__(self, gunpla_id, product):
        self.id = gunpla_id
        self.name = re.sub(r'\([^)]*\)', '', product['name']).strip()

        if 'manufacture' in product:
            self.manufacture = product['manufacture'].strip()
        else:
            self.manufacture = ''

        if 'grade' in product:
            self.grade = product['grade'].strip()
        else:
            self.grade = ''

        if 'scale' in product:
            if product['scale'] == 'Non':
                self.scale = 'Not applicable'
            else:
                self.scale = product['scale'].strip()
        else:
            self.scale = ''

        if 'series' in product:
            self.series = product['series'].strip()
        else:
            self.series = ''

        if 'release date' in product:
            if product['release date'] != 'Pre-Order':
                self.release_date = re.sub(
                    r'^\W*\w+\W*',
                    '',
                    product['release date']).replace(
                    '.',
                    '')
            else:
                self.release_date = 'Not yet released'
        else:
            self.release_date = ''

        try:
            self.release_date_code = datetime.datetime.strptime(
                self.release_date,
                '%b, %Y')
        except:
            self.release_date_code = None

        if self.release_date_code is not None:
            utc_release_date = pytz.utc.localize(self.release_date_code)
            self.release_date_code = utc_release_date

        self.name = self.name.upper()
        self.manufacture = self.manufacture.upper()
        self.scale = self.scale.upper()
        self.series = self.series.upper()
        self.release_date = self.release_date.upper()

    def __str__(self):
        return ('ID: {} \nNAME: {} \nGRADE: {}\nMANUFACTURE: {} \n'
                'SCALE: {} \nSERIES: {} \nRELEASE DATE: {}\n'
                'DATE: {}'.format(self.id, self.name, self.grade,
                                  self.manufacture, self.scale, self.series,
                                  self.release_date, self.release_date_code))

    '''
    Prints the gunpla information summarized.
    '''

    def summary(self):
        return ('ID: {} \nNAME: {} \nGRADE: {}\nMANUFACTURE: {} \n'
                'SCALE: {} \nSERIES: {} \nRELEASE DATE: {}\n'
                'DATE: {}'.format(self.id, self.name, self.grade,
                                  self.manufacture, self.scale, self.series,
                                  self.release_date, self.release_date_code))

    '''
    Adds the gunpla to the database.
    '''

    def insert(self):
        gunpla_dao = GunplaDAO()
        try:
            print('{} registered succesfully. ObjectID: {}.'
                  .format(self.name, gunpla_dao.insert(self)
                          .inserted_id))
        except pymongo.errors.ExecutionTimeout:
            print('Error while inserting item. Execution Timeout.')
        except Exception:
            print('Error while inserting item: {}'.format(Exception))

    '''
    Finds if a gunpla is already on the database.
    '''

    def find(self):
        gunpla_dao = GunplaDAO()
        gunpla_found = gunpla_dao.find(self)
        if gunpla_found is None:
            return None
        else:
            self.id = gunpla_found['item_id']
            self.name = gunpla_found['name']
            self.manufacture = gunpla_found['manufacture']
            self.grade = gunpla_found['grade']
            self.scale = gunpla_found['scale']
            self.series = gunpla_found['series']
            self.release_date = gunpla_found['release date']
            self.release_date_code = gunpla_found['release date code']
            self.added = gunpla_found['added']
        return self

    '''
    Removes a gunpla from the database.
    '''

    def remove(self):
        gunpla_dao = GunplaDAO()
        if not gunpla_dao.remove(self):
            return True
        else:
            return False

    '''
    Updates a gunpla on the database.
    '''

    def update(self):
        self.remove()
        self.insert()
