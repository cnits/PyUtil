from xml.etree.ElementTree import *
import os


class XmlParser:
    def __init__(self, xml, encoding="utf-8"):
        self.encoding = encoding
        self.element = None
        if xml is None:
            raise ValueError("Xml source is none!")
        else:
            if os.path.exists(xml):
                self.element = self.__parse(xml).getroot()
            else:
                self.element = self.__to_xml(xml)

    @staticmethod
    def __parse(_file):
        return parse(_file)

    @staticmethod
    def __to_xml(xml):
        return XML(xml)

    def get_element(self):
        return self.element
