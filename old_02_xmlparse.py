import xml.etree.ElementTree as ET

def categ(oid):
	cat_list=oid.keys()
	ban_list=['Debug','License Management']
	for item in ban_list:
		cat_list.remove(item)
	return cat_list

def oid(category):
	col_width = max(len(word) for row in oids[category].items() for word in row) + 4
	for key in oids[category].items():
		print "".join(word.ljust(col_width) for word in key)
		
def print_cat(cat_list):
	for item in cat_list:
		print "\t",item
	cat=raw_input("\nEnter category: ")
	return cat

def get_file(prompt, mode):
    while True:
        try:                                    
            return open(raw_input(prompt), mode) 
        except OSError as error:
            print error
	
file=get_file('Enter filename: ', 'r')
data=file.read()
tree = ET.fromstring(data)
xml = tree.findall('.Element')

oids={}
for element in xml:
	oids[element.get('Name')]={}
	a=element.findall('Element/Parameters/Parameter')
	for item in a:
		oids[element.get('Name')][item.find('Visualization/Name').text]=item.get('ID') 

		
cat_list=categ(oids)

category=print_cat(cat_list)
oid(category)
