'''
--------------------------------------------------------------------------------------------------------
loads credits via xml
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from menu_scripts import xml_parse

global credits_list
global add_title
global names_list
global add_name
global last_added_title
global goto_menu

cont = logic.getCurrentController()
own = cont.owner

credits_list = []
names_list = []
last_added_title = None
add_title = cont.actuators['add_title']
add_name = cont.actuators['add_name']


def init():
	global credits_list
	credits_list = xml_parse.readXML('credits.xml', ['section'], True)

def main():
	global credits_list
	global last_added_title
	
	cont = logic.getCurrentController()
	
	goto_menu = cont.actuators['goto_menu']
	#title_font = logic.getCurrentScene().objects['title_font']
	
	if own['names'] != True:
		if own['credits_start'] >=5:
			if credits_list != []:
				send_title()
				own['credits_start'] = 0
				own['names'] = True
			else:
				cont.activate(goto_menu)
	else:
		if own['credits_start'] >=3.5:
			if names_list != []:
				send_name()
				own['credits_start'] = 0
			else:
				own['names'] = False
				last_added_title['gone'] = True
		
def send_title():
	global credits_list
	global add_title
	global names_list
	global last_added_title
	
	section = credits_list[0]
	section_id = section.get('id')
	section_title = section.get('title')
	credits_list.remove(section)
	add_title.instantAddObject()
	added_title = add_title.objectLastCreated
	
	#setup title text & position it in the center of the screen
	added_title.text = section_title
	d_length = len(added_title.text)
	added_title.text.center
	last_added_title = added_title
	
	name_check = section.find('name')
	if name_check != None:
		names = list(section.iter('name'))
		names_list = names
		for name in names:
			print (name.text)

def send_name():
	global names_list
	global add_name
	
	name = names_list[0]
	name_text = name.text
	names_list.remove(name)
	add_name.instantAddObject()
	added_name = add_name.objectLastCreated
	
	added_name.text = name_text
	
	d_length = len(added_name.text)
	added_name.text.center
	#added_name.position[0] = (-d_length *.725)