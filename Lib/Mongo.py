from pymongo import MongoClient


class MongoDB:
    def __init__(self, host, port):
        if host is None or host == "":
            host = 'localhost'
        if port is None or port == "":
            port = 27017
        self.dbm = MongoClient(host, port)


