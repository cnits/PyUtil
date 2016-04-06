from lxml import etree, builder, html
from io import StringIO, BytesIO
import os


class CPyLXmlParser:
    def __init__(self, xstr, encoding="utf-8"):
        self.encoding = encoding
        self.xstr = None
        if xstr is None:
            raise ValueError("Source content is none!")
        else:
            self.xstr = xstr

    def parse(self, is_xml=True):
        parser = etree.XMLParser()
        if is_xml is False:
            parser = etree.HTMLParser()
        return etree.parse(self.xstr, parser)

    def str_to_element(self):
        return html.fromstring(self.xstr)
