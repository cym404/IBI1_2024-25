import xml.dom.minidom
import datetime

start_time_dom = datetime.datetime.now()
dom_tree = xml.dom.minidom.parse(r"C:\Users\lenovo\Desktop\新建文件夹\IBI1_2024-25\practical14\go_obo.xml")
collection = dom_tree.documentElement
terms = collection.getElementsByTagName('term')

max_is_a_count = 0
max_term = None
for term in terms:
    is_a_elements = term.getElementsByTagName('is_a')
    count = len(is_a_elements)
    if count > max_is_a_count:
        max_is_a_count = count
        max_term = term

print(f"The GO term with the most <is_a> elements: {max_term.getElementsByTagName('name')[0].firstChild.data}")
print(f"Number of <is_a> elements: {max_is_a_count}")

end_time_dom = datetime.datetime.now()
time_taken_dom = (end_time_dom - start_time_dom).total_seconds()

import xml.sax
import datetime


class TermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_term = None
        self.is_a_count = 0
        self.max_is_a_count = 0
        self.max_term = None

    def startElement(self, tag, attributes):
        if tag == 'term':
            self.current_term = {}
            self.is_a_count = 0
        elif tag == 'is_a':
            self.is_a_count += 1
        elif tag=='name':
            self.current_name=""

    def endElement(self, tag):
        if tag == 'term':
            if self.is_a_count > self.max_is_a_count:
                self.max_is_a_count = self.is_a_count
                self.max_term = self.current_term
                self.max_term['name']=self.current_name
            elif tag=='name':
                self.current_term['name']=self.current_name

start_time_sax = datetime.datetime.now()
handler = TermHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(r"C:\Users\lenovo\Desktop\新建文件夹\IBI1_2024-25\practical14\go_obo.xml")

print(f"The GO term with the most <is_a> elements: {handler.max_term.get('name', 'Unknown')}")
print(f"Number of <is_a> elements: {handler.max_is_a_count}")

end_time_sax = datetime.datetime.now()
time_taken_sax = (end_time_sax - start_time_sax).total_seconds()

if time_taken_dom < time_taken_sax:
    print(f"DOM API took {time_taken_dom} seconds, SAX API took {time_taken_sax} seconds. DOM API is faster.")
else:
    print(f"DOM API took {time_taken_dom} seconds, SAX API took {time_taken_sax} seconds. SAX API is faster.")