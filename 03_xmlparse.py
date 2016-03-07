class oids(object):														# Class that handles XML parsing/printing
	oid={}																# Creating of a dictionary - will contain parsed elements
	cat_list=[]															# Creating of a list - will contain categories names
	cat_ban_list=['Debug','License Management', 'Advanced Statistics']	# Creating of a ban list - will define elements that shouldn't be in the categories
	wlist=[]
	def __init__(self, fhandle):										# Class oids constructor - parse XML, populate oid{} and creating/modifying category list
		import xml.etree.ElementTree as ET								# So on...
		data=fhandle.read()
		tree = ET.fromstring(data)
		xml = tree.findall('.Element')
		for element in xml:
			self.oid[element.get('Name')]={}
			a=element.findall('Element/Parameters/Parameter')
			for item in a:
				self.oid[element.get('Name')][item.find('Visualization/Name').text]=item.get('ID')
		
		self.cat_list=self.oid.keys()
		for item in self.cat_ban_list:
			try:
				self.cat_list.remove(item)
			except:
				continue

	def oid_print(self,category, write=False):
		if not self.oid[category].items(): print "Category is empty!"
		else:
			col_width = max(len(word) for row in self.oid[category].items() for word in row) + 4	# Takes a category and makes output of OIDs (user friendly)
			for key in self.oid[category].items():
				if write==False:
					print "".join(word.ljust(col_width) for word in key).strip()
				else:
					self.wlist.append("".join(word.ljust(col_width) for word in key).strip())
	
	def excel(self,exc_file=None,categories='All'):
		import xlwt
		s=0
		wb = xlwt.Workbook()
		ws = wb.add_sheet('OIDs')
		font0 = xlwt.Font()
		font0.bold = True
		style1 = xlwt.XFStyle()
		style1.font = font0
		
		if not exc_file:
			while True:
				exc_file=raw_input("Enter excel filename: ")	
				if len(exc_file)>2: break
				else: print "Name length should be > 2: "
		if categories=='All':
			categories=self.cat_list
		if (type(categories) is list) or (categories=='All'):
			for item in categories:
				s+=2
				ws.write(s, 0, item.upper(), style1)
				for elements in self.oid[item].items():
					s+=1
					ws.write(s, 0, elements[0])
					ws.write(s, 1, elements[1])					

		elif type(categories) is not list:						#In case we need to print one category (not list of them or all)
			ws.write(s, 0, categories.upper(), style1)
			for elements in self.oid[item].items():
				s+=1
				ws.write(s, 0, elements[0])
				ws.write(s, 1, elements[1])
		ws.col(0).width=int(30*256)
		ws.col(1).width=int(20*256)
		wb.save(exc_file+'.xls')
		print "### Saved ###"
		raw_input()			

	def txt(self, txt_file):
		for category in self.cat_list:
			txt_file.handle.write('\n'+category+'\n')
			self.oid_print(category, write=True)
			for item in self.wlist:
				txt_file.handle.write(item+'\n')
		print "### Saved ###"
		raw_input()
				
class menu(object):									# Class for dynamical creating/printing/taking menu elements 
	flist=[]
	fmt_list=[]
	n=1
	def print_cat(self, cat_list):					# Takes a list and makes an list of tuples. Ex: ['a','b','c'] -> [(1,'a'),(2,'b'),(3,'c')]
		self.n=1
		self.fmt_list=[]
		for item in cat_list:
			self.fmt_list.append((self.n, item))
			self.n+=1
		for item in self.fmt_list:					# Prints the formatted list
			print item[0],":", item[1]
			
	def get_cat(self):								# Takes user input and fmt_list, returns name of category based on category number
		cat=0
		while True:
			ch=raw_input("\nEnter # (q-quit) > ")
			print "\n"
			if ch=='q': exit()
			try:
				ch=int(ch)
				for item in self.fmt_list:
					if ch==item[0]:
						cat=item[1]
						break
				if cat!=0: break
				else:
					print "No such instance. Please correct!"
			except:
				print "Wrong chose! Please correct."
		return cat	
		
	def flist(self):								# List all XML files in directory
		import glob
		flist=glob.glob("*.xml")
		self.print_cat(flist)

		
class files(object):
	name=''
	def get_u(self, prompt, mode):					# Open a file based on console(user) input
		while True:
			try:
				name=raw_input(prompt)
				self.handle=open(name, mode)
				break
			except OSError as error:
				print error
				
	def get(self, input, mode):						# Open a file based on given argument
		while True:
			try:                                    
				self.handle=open(input, mode)
				break
			except OSError as error:
				print error	

def main():	
	file=files()
	fm=menu()
	fm.flist()	
	fname=fm.get_cat()		
	file.get(fname, 'r')

	m=menu()
	temp=oids(file.handle)
	menu_lst=['On the screen','To the excel','To the .txt','Exit',':about']
	mmenu=menu()
	chose=0

	while True:
		mmenu.print_cat(menu_lst)
		chose=mmenu.get_cat()
		
		if chose==menu_lst[0]:
			while True:
				m.print_cat(temp.cat_list)
				temp.oid_print(m.get_cat())
				i=raw_input("\n> ")
				if i=='b': break
				
		elif chose==menu_lst[1]:
			temp.excel()
			
		elif chose==menu_lst[2]:
			wfile=files()
			wfile.get_u('Write: Enter filename: ', 'w+')
			temp.txt(wfile)

		elif chose==menu_lst[3]:
			exit()

		elif chose==menu_lst[4]:
			print "SEII component template XML parser\n"
			print "Source: https://github.com/gangand/oop_project\n"
			raw_input()

		else: pass

if __name__ == '__main__':
    main()