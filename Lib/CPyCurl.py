try:
    from urllib.request import *
    from urllib.parse import *
    from urllib.error import *
    from urllib.response import *
except ImportError:
    from urllib2 import *
    import urllib


class CPyCurl:
    def __init__(self, url, params):
        self.Url = url
        if params is not None:
            try:
                self.Data = urlencode(params).encode('utf-8')
            except:
                self.Data = urllib.urlencode(params).encode('utf-8')
        else:
            self.Data = ""

    def do_request(self, headers):
        try:
            if self.Data == "":
                query = Request(self.Url)
            else:
                query = Request(self.Url, self.Data)
            if headers is not None:
                for i in headers:
                    query.add_header(i, headers[i])
            return urlopen(query).read()
        except URLError as er:
            print(er.reason)
