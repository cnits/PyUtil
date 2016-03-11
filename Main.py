from Lib.Curl import *
if __name__ == "__main__":
    try:
        # curl = Curl("http://pythonprogramming.net", {'s': 'basic', 'submit': 'search'})
        curl = Curl("https://raw.githubusercontent.com/cnits/cnit/master/books.xml", None)
        response = curl.do_request(None)

        print(response)
    except Exception as ex:
        print(str(ex))
