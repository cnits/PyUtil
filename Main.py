from Lib.Curl import *
from Lib.Mongo import *


def mongo_test():
    db = MongoDB("test", None, None)
    # data = db.find('test', {'Id': 3})
    # data = db.find_one('test', None)
    data = db.distinct('test', "Name", None)
    print(data)


def curl_test():
    # curl = Curl("http://pythonprogramming.net", {'s': 'basic', 'submit': 'search'})
    curl = Curl("https://raw.githubusercontent.com/cnits/cnit/master/books.xml", None)
    response = curl.do_request(None)
    print(response)

if __name__ == "__main__":
    try:

        mongo_test()
    except Exception as ex:
        print(str(ex))
