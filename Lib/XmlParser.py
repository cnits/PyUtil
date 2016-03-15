from xml.etree.ElementTree import *


class XmlParser:
    def __init__(self, encoding="utf-8"):
        self.encoding = encoding
        pass

    def parse(self, _file):
        return parse(_file)

    def to_xml_element(self, xml):
        return XML(xml)
