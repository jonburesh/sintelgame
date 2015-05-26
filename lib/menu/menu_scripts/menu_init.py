'''
--------------------------------------------------------------------------------------------------------
script that runs the menu functions
handles selecting items
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render
from menu_scripts import xml_parse
from menu_scripts import set_defualt_vars

cont = logic.getCurrentController()
own = cont.owner

obj_list = logic.getCurrentScene().objects
resume_game = logic.getCurrentScene().objects['resume_option']

menu_items = []

menu_music = cont.actuators['menu_music']

def test_save():
	try:
		logic.loadGlobalDict()
		if logic.globalDict['player_pos'] != None:
			return True
		else:
			return False
	except:
		return False
		
def set_app_ver():
	#get the whole xml file
	menu_xml = xml_parse.readXML('menu.xml', False, False)

	version_text = logic.getCurrentScene().objects['version_text']
	notice_text = logic.getCurrentScene().objects['notice_text']

	resume_game = logic.getCurrentScene().objects['resume_option']
	new_game = logic.getCurrentScene().objects['new_game_option']
	extras_option = logic.getCurrentScene().objects['extras_option']
	options_item = logic.getCurrentScene().objects['options_item']
	exit_option = logic.getCurrentScene().objects['exit_option']
	
	#set app version number
	app_version = menu_xml.find('version')
	version_text.text = app_version.text
	
	#set the notice text
	notice = menu_xml.find('notice')
	notice_text.text = notice.text
	
	#set menu button text
	resume = menu_xml.find('resume')
	resume_game['text'] = resume.text
	#so on
	new_game_text = menu_xml.find('new')
	new_game['text'] = new_game_text.text
	#and so forth
	extras = menu_xml.find('extra')
	extras_option['text'] = extras.text
	
	options = menu_xml.find('options')
	options_item['text'] = options.text
	
	exit = menu_xml.find('exit')
	exit_option['text'] = exit.text
	#start the music!
	menu_music.startSound()
	
	#if the sintel film is included
	include_film = menu_xml.find('include_film')
	
	if include_film.text =='True':
		logic.globalDict['include_film'] = True
	else:
		logic.globalDict['include_film'] = False

for ob in obj_list:
	if 'ID' in ob:
		menu_items.append(ob)
		#print (menu_items)
if test_save():
	print ('Found Save File')
	resume_game['next_level'] = logic.globalDict['Load_Next']
else:
	#no acceptable save file found, remove resume menu option
	set_defualt_vars.main(True)
	resume_game['selectable'] = False
	for i in resume_game.children:
		i.visible = 0
	menu_items.pop()
	#print (menu_items)

mouse_move = own.sensors['mouse_move']
mouse_over = own.sensors['mouse_over']
mouse_click = own.sensors['mouse_click']
enter_key = own.sensors['enter_key']
up_key = own.sensors['up_key']
down_key = own.sensors['down_key']

logic.MENU_CURRENT_SUB_ID = 0
logic.MENU_CURRENT_ID = 1

render.showMouse(1)
set_app_ver()

def main():
	if enter_key.positive:
		set_active(get_ID(logic.MENU_CURRENT_ID))
		
	if mouse_move.positive:
		own['mouse_timer'] +=1
		if own['mouse_timer'] >=15:
			own['mouse_movement'] = True
		
	if own['mouse_movement'] == True:
		if mouse_over.hitObject != None:
			OVER = mouse_over.hitObject.parent
			try:
				if 'selected' in OVER:
					if OVER['selectable'] == True:	
						set_sel(OVER)
				if mouse_click.positive:
					if OVER['selectable'] == True:	
						set_active(OVER)
			except:
				pass

	if up_key.positive or down_key.positive:
		own['mouse_movement'] = False
		own['mouse_timer'] =0
		
	if up_key.positive:
		new_ID = logic.MENU_CURRENT_ID -1
		try:
			set_sel(get_ID(new_ID))
		except:
			try:
				set_sel(get_ID(0))
			except:
				set_sel(get_ID(1))
	if down_key.positive:
		new_ID = logic.MENU_CURRENT_ID +1
		try:
			set_sel(get_ID(new_ID))
		except:
			try:
				set_sel(get_ID(0))
			except:
				set_sel(get_ID(1))
		
def get_ID(ID):
	for items in menu_items:
		if items['ID'] == ID:
			return items
	else:
		return False
		
def set_active(item):
	item['active'] = True
	if item['ID'] == 1:
		logic.globalDict['game_load'] = False
		set_defualt_vars.main(False)
		#logic.saveGlobalDict()
		#render.showMouse(0)
	if item['ID'] == 0:
		menu_music.volume = 0
		menu_music.stopSound()
		cont.deactivate(menu_music)
		logic.globalDict['game_load'] = True
		logic.globalDict['Load_Next'] = logic.globalDict['level_name']
		print ('setting loading file to:',logic.globalDict['Load_Next'])
		logic.saveGlobalDict()
		render.showMouse(0)
		
	
def set_sel(item):
	logic.MENU_CURRENT_ID = item['ID']
	logic.MENU_CURRENT_SUB_ID = item['sub_ID']
	
	item['selected'] = True
	for items in menu_items:
		if items != item:
			items['selected'] = False