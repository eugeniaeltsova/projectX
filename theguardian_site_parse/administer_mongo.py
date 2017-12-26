from pymongo import MongoClient
from theguardian_site_parse.settings import *


def connect():
    connect_address = "mongodb://{}:{}@{}:{}/{}".format(USER, PASS, HOST, PORT, DB_NAME)
    client = MongoClient(connect_address)
    db = getattr(client, DB_NAME)
    return db


def write_one(obj, dict_article):
    obj.articles.insert_one(dict_article)
    return True


def read_all(obj, collection):
    """return all result for collection. Warnings, if articles very more, it's may be call soo long process running"""
    result = []
    collect_db = getattr(obj, collection)
    for step in collect_db.find():
        result.append(step)
    return result


if __name__ == '__main__':
    print("start")
    # article = json.loads(open('main/articles/article_1.txt', 'r').read())
    obj_db = connect()
    get_all = read_all(obj_db, 'articles')
    print(type(get_all[0]))
    print(type(get_all[0]['_id']))
    print(get_all)

