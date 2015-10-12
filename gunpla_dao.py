import datetime
from pymongo import MongoClient

__author__ = 'porthunt'

'''
Adds the gunpla to the database.
'''


class GunplaDAO(object):

    # database: 'mobilesuit_db'
    # collection: 'mobilesuit'

    '''
    Inserts a Gunpla object into the mongoDB database.
    '''
    def insert(self, gunpla):
        client = MongoClient()
        gunpla_dic = {'item_id': gunpla.id,
                      'name': gunpla.name,
                      'manufacture': gunpla.manufacture,
                      'grade': gunpla.grade,
                      'scale': gunpla.scale,
                      'series': gunpla.series,
                      'release date': gunpla.release_date,
                      'release date code': gunpla.release_date_code,
                      'added': datetime.datetime.now()}

        database = client.mobilesuit_db
        return database.mobilesuit.insert_one(gunpla_dic)

    def find(self, gunpla):
        client = MongoClient()
        database = client.mobilesuit_db
        return database.mobilesuit.find_one({"item_id": gunpla.id})

    def remove(self, gunpla):
        client = MongoClient()
        database = client.mobilesuit_db
        return database.mobilesuit.remove({"item_id": gunpla.id})
