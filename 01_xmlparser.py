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

tree = ET.parse('Access_06.55.00.74_Template.xml')
root = tree.getroot()
print root.attrib['Version']
oids={}
categories=[]
for child in root:
	if (child.tag=='Element' and child.attrib['Name']!='License Management'):
		categories.append(child.attrib['Name'])
		oids[child.attrib['Name']]={}
		for child2 in child:
			if (child2.tag=='Element'):
				for child3 in child2:
					if child3.tag == 'Element':
						oids[child.attrib['Name']][child3.tag['Name']]={}
					for child4 in child3:
						if child4.tag == 'Parameters':
							for child5 in clild4:	
								name = child5.attrib['ID']
								if child5.tag=='Visualization':
									oids[child.attrib['Name']][child5.find('Name').text]=name
print_cat(categories)