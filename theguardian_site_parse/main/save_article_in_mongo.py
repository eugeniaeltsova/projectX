
# This script open dir articles and save in mongodb
# Process send std_out
# I'm save in mongodb 326 articles

import json
import os

from theguardian_site_parse.administer_mongo import connect, write_one

c_obj = connect()
list_file = os.listdir('articles')
list_file.remove('articles')
index = 0

for name_file in list_file:
    body = json.loads(open('articles/' + name_file, 'r').read())
    if write_one(c_obj, body):
        print("success number {} for article {}".format(index, name_file))
        index += 1

