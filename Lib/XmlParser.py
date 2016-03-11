from xml.etree.ElementTree import *

class XmlParser:
    def __init__(self):
        self.id = range(1)

    def parse(self, _file):
        return parse(_file)

    def to_xml_element(self, xml):
        return XML(xml)


