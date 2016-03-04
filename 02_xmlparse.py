import xml.etree.ElementTree as ET

def oid(category):
	col_width = max(len(word) for row in oids[category].items() for word in row) + 4
	for key in oids[category].items():
		print "".join(word.ljust(col_width) for word in key)
		
def print_cat(cat_list):
	for item in cat_list:
		print "\t",item
	cat=raw_input("\nEnter category: ")
	oid(cat)
file=open('Access_06.55.00.74_Template.xml')
data=file.read()
tree = ET.fromstring(data)
xml = tree.findall('.Element')
print type(xml)
for element in xml:
	a=element.findall('Element/Parameters/Parameter')
	for item in a:
		print item.get('ID') 
		print item.find('Visualization/Name').text
