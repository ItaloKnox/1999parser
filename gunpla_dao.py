__author__ = 'porthunt'

from pymongo import MongoClient
import datetime

'''
Adds the gunpla to the database.
'''

class GunplaDAO(object):

    #database: 'mobilesuit_db'
    #collection: 'mobilesuit'

    '''
    Inserts a Gunpla object into the mongoDB database.
    '''
    def insert(self, client, gunpla):

        gunpla_dic = { 'item_id': gunpla.id,
                       'name': gunpla.name,
                       'manufacture': gunpla.manufacture,
                       'grade': gunpla.grade,
                       'scale': gunpla.scale,
                       'series': gunpla.series,
                       'release date': gunpla.release_date,
                       'release date code': gunpla.release_date_code,
                       'added': datetime.datetime.now()
                     }

        database = client.mobilesuit_db
        try:
            result = database.mobilesuit.insert_one(gunpla_dic)
            return result
        except pymongo.errors.DuplicateKeyError:
            raise ValueError('Duplicate entry on the database.')
        except pymongo.errors.ExecutionTimeout:
            raise ValueError('Could not connect to the database.')
        except:
            raise ValueError('Could not insert to the collection.')
