from Lib.CPyCurl import *
from Lib.CPyMongo import *
from Lib.CPyFile import *
from Lib.CPyXmlParser import *
from Lib.CPyEquipment import CPyEquipment
from Lib.CPyLXmlParser import *


def equipment_test():
    eq = CPyEquipment("172.16.4.")
    eq.test()

def mongo_test(j_data):
    db = CPyMongo("test", None, None)
    # data = db.find('test', {'Id': 3})
    # data = db.find_one('test', None)
    # data = db.distinct('test', "Name", None)
    db.save("books", j_data, True)


def curl_test():
    # curl = Curl("http://pythonprogramming.net", {'s': 'basic', 'submit': 'search'})
    # curl = CPyCurl("https://raw.githubusercontent.com/cnits/cnit/master/books.xml", None)
    curl = CPyCurl("http://ccicore.devhost/silverpeak/runin_smart/latest/latest.php", {
        'serial': '001BBC122B2A'
    })
    return curl.do_request(None)


def file_test():
    path = "files/book_info.txt"
    try:
        pyFile = CPyFile(path)
        lines = pyFile.read_lines("r")
        print(lines)
    except Exception as ex:
        print(str(ex))


def xml_test(xml):
    x_parse = CPyXmlParser(xml)
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
        # x_data = xml_test(response)
        # mongo_test(x_data)
        # opts, args = getopt.getopt(sys.argv[1:], "hg:d", ["help"])
        # print(sys.argv[1:])
        # file_test()
        # equipment_test()
        d = CPyLXmlParser(response)
        print(d.parse(False).xpath('//a/text()'))
    except Exception as ex:
        print(str(ex))
