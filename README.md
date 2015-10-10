# 1999parser
Tool to compile data about 1999.co.jp products and insert them on a MongoDB database. Built for gundam plastic models.

# Parsed info
- Name
- Grade
- Manufacturer
- Scale
- Original Series
- Release Date

# Image format
For all images: http://www.1999.co.jp/eng/image/[product_code][A-Z]/[10-90]/[1-10]

For [box covers](http://www.1999.co.jp/eng/image/10334864p/10/1): /[product_code]p/10/1 

For [completed model photos](http://www.1999.co.jp/eng/image/10334864a/20/1): /[product_code]a/20/1 (>> /[product_code]a[2-99]/20/[2-99])

# Required libraries
>You may want to use Python 2.7 instead of 3.X.

- datetime
- HTMLParser
- pymongo
- pytz
- re
- requests

>Use **pip install**

# Required steps
* Install MongoDB (Mongo Shell > 3.X).
* Create an index on the database:
  * *$ mongo* 
  * *> use mobilesuit_db*
  * *> db.mobilesuit.createIndex({'item_id' : 1}, {'unique' : 1})*

