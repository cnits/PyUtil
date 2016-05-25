from lxml import etree, builder, html
from io import StringIO, BytesIO
import os

'''
HTML Element Methods
HTML elements have all the methods that come with ElementTree, but also include some extra methods:
	.drop_tree(): Drops the element and all its children. Unlike el.getparent().remove(el) this does
not remove the tail text; with drop_tree the tail text is merged with the previous element.

	.drop_tag(): Drops the tag, but keeps its children and text.

	.find_class(class_name): Returns a list of all the elements with the given CSS class name. Note that
class names are space separated in HTML, so doc.find_class_name("highlight") will find an
element like <div class="sidebar highlight">. Class names are case sensitive.

	.find_rel_links(rel): Returns a list of all the <a rel="{rel}"> elements. E.g., doc.find_rel_links("tag")
returns all the links marked as tags.

	.get_element_by_id(id, default=None): Return the element with the given id, or the default if
none is found. If there are multiple elements with the same id (which there shouldn't be, but there often is),
this returns only the first.

	.text_content(): Returns the text content of the element, including the text content of its children, with no
markup.

	.cssselect(expr): Select elements from this element and its children, using a CSS selector expression.
(Note that .xpath(expr) is also available as on all lxml elements.)

	.label: Returns the corresponding <label> element for this element, if any exists (None if there is none).
Label elements have a label.for_element attribute that points back to the element.

	.base_url: The base URL for this element, if one was saved from the parsing. This attribute is not settable. Is
None when no base URL was saved.

	.classes: Returns a set-like object that allows accessing and modifying the names in the "class" attribute of
the element. (New in lxml 3.5).
'''


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
