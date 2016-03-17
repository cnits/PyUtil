import pycurl
import re
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class CPyCurlLib:
    def __init__(self, url):
        self.Url = url

    def __get_instance(self):
        pcu = pycurl.Curl()
        pcu.setopt(pcu.URL, self.Url)
        return pcu

    def header_func(self, header):
        return 1

    def set_opts(self, opts):
        # for item in opts:
            # self.PCUrl.setopt(item.property, item.value)
        pass

    def do_request(self, encoding=None):
        _buffer = BytesIO()
        pcu = self.__get_instance()
        pcu.setopt(pcu.WRITEFUNCTION, _buffer.write)
        # pcu.setopt(pcu.WRITEDATA, buffer)
        # pcu.setopt(pcu.HEADERFUNCTION, header_func({}))
        pcu.perform()
        pcu.close()
        if encoding is None:
            encoding = 'iso-8859-1'
        data = _buffer.getvalue()
        return data.decode(encoding)

    def post_request(self, data):
        """
        Form data must be provided already urlencoded.
        Sets request method to POST,
        Content-Type header to application/x-www-form-urlencoded
        and data to send in request body.
        """
        pcu = self.__get_instance()
        pcu.setopt(pcu.POSTFIELDS, urlencode(data))
        pcu.perform()
        pcu.close()

    def write_to_file(self, _file):
        pcu = self.__get_instance()
        pcu.setopt(pcu.WRITEDATA, _file)
        pcu.perform()
        pcu.close()

    def file_upload(self, path_file, is_buffer=False):
        pcu = self.__get_instance()
        if is_buffer is True:
            pcu.setopt(pcu.HTTPPOST, [
                ('fileupload', (
                    pcu.FORM_BUFFER, 'fancy.file',
                    pcu.FORM_BUFFERPTR, 'This is a fancy readme file',
                )),
            ])
        else:
            pcu.setopt(pcu.HTTPPOST, [
                ('fileupload', (
                    # upload the contents of this file
                    # pcu.FORM_FILE, __file__,
                    # specify a different file name for the upload
                    pcu.FORM_FILENAME, path_file,
                    # specify a different content type
                    # pcu.FORM_CONTENTTYPE, 'application/x-python',
                )),
            ])
        pcu.perform()
        pcu.close()
