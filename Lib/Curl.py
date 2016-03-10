import urllib.request as u_request
import urllib.parse as u_parse
import urllib.error as u_error
import urllib.response as u_response


class Curl:
    def __init__(self, url, params):
        self.Url = url
        if params is not None:
            self.Data = u_parse.urlencode(params).encode('utf-8')
        else:
            self.Data = ""

    def do_request(self, headers):
        try:
            if self.Data == "":
                query = u_request.Request(self.Url)
            else:
                query = u_request.Request(self.Url, self.Data)
            if headers is not None:
                for i in headers:
                    query.add_header(i, headers[i])
            return u_request.urlopen(query).read()
        except u_error.URLError as er:
            print(er.reason)
