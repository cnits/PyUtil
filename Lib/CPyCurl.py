import urllib.request
import urllib.parse
import urllib.error
import urllib.response


class CPyCurl:
    def __init__(self, url, params):
        self.Url = url
        if params is not None:
            self.Data = urllib.parse.urlencode(params).encode('utf-8')
        else:
            self.Data = ""

    def do_request(self, headers):
        try:
            if self.Data == "":
                query = urllib.request.Request(self.Url)
            else:
                query = urllib.request.Request(self.Url, self.Data)
            if headers is not None:
                for i in headers:
                    query.add_header(i, headers[i])
            return urllib.request.urlopen(query).read()
        except urllib.error.URLError as er:
            print(er.reason)
