import xml.etree.ElementTree as ET
import os

def readXML(xml_file, attributes, is_list):
	print ('\n------------------------------\nreading file: %s...\n------------------------------\n' % (xml_file))
	file_name = os.path.abspath(__file__)
	file_name = os.path.dirname(file_name)
	file_name = os.path.join(file_name, xml_file)
	#print (file_name)
	
	tree = ET.parse(file_name)
	root = tree.getroot()
	
	if not attributes:
		return tree
	else:
		if is_list:
			found_attr = list(tree.iter(attributes[0]))
			return found_attr
		else:
			try:
				found_attr = tree.find(attributes[0])
				found_attr = found_attr.text
				return found_attr
			except:
				print ('could not find given attribute')
				return False
			
def menuVer():
	readXML('menu.XML', ['version'])