from pymongo import MongoClient


def connect():
    """read settings for connect db and return MongoClient cursor"""
    connect_address = "mongodb://{}:{}@{}:{}/{}".format(USER, PASS, HOST, PORT, DB_NAME)
    client = MongoClient(connect_address)
    db = getattr(client, DB_NAME)
    return db


def write_one(obj, dict_article):
    """insert new dict in mongodb"""
    obj.articles.insert_one(dict_article)
    return True


def update_one(obj, original_dict, new_dict):
    """change structure in mongodb via update and return True"""
    obj.articles.update(original_dict, new_dict)
    return True


def read_all(obj, collection):
    """return all result for collection. Warnings, if articles very more, it's may be call soo long process running"""
    result = []
    collect_db = getattr(obj, collection)
    for step in collect_db.find():
        result.append(step)
    return result


if __name__ == '__main__':
    try:
        from .local_connect import *
    except ImportError:
        pass
