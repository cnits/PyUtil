from pymongo import MongoClient
try:
    from urllib.parse import quote_plus
except Exception:
    from urllib import quote_plus

class CPyMongo:
    def __init__(self, db_name, user=None, password=None, host=None, port=None):
        if host is None or host == "":
            host = 'localhost'
        if port is None or port == "":
            port = 27017
        try:
            if user is None or password is None:
                self.dbm = MongoClient(host, port)[db_name]
            else:
                self.dbm = MongoClient("mongodb://" + user + ":" + quote_plus(password) + "@" + host + ":" + port)[db_name]
        except Exception as ex:
            print(str(ex))

    def find(self, collection, _filter):
        if _filter is None:
            _filter = {}
        result = self.dbm[collection].find(_filter)
        data = []
        for i in result:
            data.append(i)
        return data

    def find_one(self, collection, _filter):
        data = self.dbm[collection].find_one(_filter)
        return data

    def save(self, collection, data, multiple=False):
        if multiple is False:
            return self.dbm[collection].insert_one(data)
        else:
            return self.dbm[collection].insert_many(data)

    def update(self, collection, _filter, update, multiple=False, upsert=False):
        if multiple is False:
            return self.dbm[collection].update_one(_filter, update, upsert)
        else:
            return self.dbm[collection].update_many(_filter, update, upsert)

    def delete(self, collection, _filter, multiple=False):
        if multiple is False:
            return self.dbm[collection].delete_one(_filter)
        else:
            return self.dbm[collection].delete_many(_filter)

    def count(self, collection, _filter):
        return self.dbm[collection].count(_filter)

    def distinct(self, collection, key, _filter):
        return self.dbm[collection].distinct(key, _filter)

    def drop(self, collection):
        self.dbm[collection].drop()

    