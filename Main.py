from Lib.Curl import *
from Lib.Mongo import *
from Lib.PyFile import *
from Lib.XmlParser import *


def mongo_test(j_data):
    db = MongoDB("test", None, None)
    # data = db.find('test', {'Id': 3})
    # data = db.find_one('test', None)
    # data = db.distinct('test', "Name", None)
    db.save("books", j_data, True)


def curl_test():
    # curl = Curl("http://pythonprogramming.net", {'s': 'basic', 'submit': 'search'})
    curl = Curl("https://raw.githubusercontent.com/cnits/cnit/master/books.xml", None)
    return curl.do_request(None)


def file_test():
    path = "files/book_info.txt"
    try:
        pyFile = PyFile(path)
        lines = pyFile.read_lines("r")
        print(lines)
    except Exception as ex:
        print(str(ex))


def xml_test(xml):
    x_parse = XmlParser(xml)
    ele_ins = x_parse.get_element()
    data = []
    for ele in ele_ins.getchildren():
        data.append({
            'bid': ele.get("id"),
            'author': ele.findtext('author'),
            'title': ele.findtext('title'),
            'genre': ele.findtext('genre'),
            'price': ele.findtext('price'),
            'publish_date': ele.findtext('publish_date'),
            'description': ele.findtext('description')
        })
    return data

if __name__ == "__main__":
    try:
        response = curl_test()
        x_data = xml_test(response)
        mongo_test(x_data)
        # opts, args = getopt.getopt(sys.argv[1:], "hg:d", ["help"])
        # print(sys.argv[1:])
        # file_test()
    except Exception as ex:
        print(str(ex))
