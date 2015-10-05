__author__ = 'porthunt'

class Gunpla(object):
    name # Gunpla name e.g. Char Aznable`s Custom Zaku II
    manufacture # Gunpla creator e.g. Bandai
    scale # Gunpla scale e.g. 1/100
    series # Gunpla origin e.g. Build Fighters
    release_date # Release date of the gunpla model e.g. Apr. 2015
    reg_price # Regular price of the gunpla e.g. 1445 yen
    
    
    def __init__(self, name, manufacture, scale, series, release_date, reg_price):
        self.name = name
        self.manufacture = manufacture
        self.scale = scale
        self.series = series
        self.release_date = release_date
        self.reg_price = reg_price
