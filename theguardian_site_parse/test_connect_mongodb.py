from pymongo import MongoClient
import json


def connect():
    connect_address = "mongodb://projectx:******@54.68.96.112:27017/projectx"
    client = MongoClient(connect_address)
    db = client.projectx
    return db


def write(obj, dict_atricle):
    obj.articles.insert_one(dict_atricle)
    print("success")

def read():
    pass

if __name__ == '__main__':
    print("start")
    article = json.loads(open('main/articles/article_1.txt', 'r').read())
    doit_obj = connect()
    print(write(doit_obj, article))