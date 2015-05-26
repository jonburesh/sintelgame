'''
--------------------------------------------------------------------------------------------------------
script that runs the extras functions
handles selecting items
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render, events
from menu_scripts import xml_parse

def init():
	global cont, own, obj_list, options_items, mouse_move, mouse_over, mouse_click, enter_key, up_key, down_key, all_keys, back_key, right_click
	cont = logic.getCurrentController()
	own = cont.owner

	obj_list = logic.getCurrentScene().objects
	film_option = logic.getCurrentScene().objects['film_option']
	
	options_items = []

	for ob in obj_list:
		if 'ID' in ob:
			options_items.append(ob)
			#print (options_items)
	
	include_film = xml_parse.readXML('menu.xml', ['include_film'], False)
	if include_film == 'False':
		film_option['selectable'] = False
		for i in film_option.children:
			i.visible = 0
		options_items.pop()
	else:
		pass
	
	mouse_move = own.sensors['mouse_move']
	mouse_over = own.sensors['mouse_over']
	mouse_click = own.sensors['mouse_click']
	right_click = own.sensors['right_click']
	enter_key = own.sensors['enter_key']
	back_key = own.sensors['back_key']
	up_key = own.sensors['up_key']
	down_key = own.sensors['down_key']
	
def setup():
	#logic.OPTIONS_CURRENT_SUB_ID = 0
	logic.OPTIONS_CURRENT_ID = 1
	render.showMouse(1)
	
def main():
	global cont, own, obj_list, options_items, mouse_move, mouse_over, mouse_click, enter_key, up_key, down_key, all_keys, back_key, right_click
	try:
		logic.OPTIONS_CURRENT_ID
	except:
		setup()
	
	#init()
	if enter_key.positive:
		set_active(get_ID(logic.OPTIONS_CURRENT_ID))
		
	if back_key.positive or right_click.positive:
		obj_list['extras_return']['active'] = True
		logic.OPTIONS_CURRENT_ID = 1
		
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
		new_ID = logic.OPTIONS_CURRENT_ID -1
		try:
			set_sel(get_ID(new_ID))
		except:
			set_sel(get_ID(0))
			
	if down_key.positive:
		new_ID = logic.OPTIONS_CURRENT_ID +1
		try:
			set_sel(get_ID(new_ID))
		except:
			set_sel(get_ID(0))

def get_ID(ID):
	#print (ID)
	for items in options_items:
		if items['ID'] == ID:
			return items
	else:
		return False
		
def set_active(item):
	item['active'] = True
	if item['ID'] ==2:
		logic.OPTIONS_CURRENT_ID = 1
		
def set_sel(item):
	logic.OPTIONS_CURRENT_ID = item['ID']
	#logic.OPTIONS_CURRENT_SUB_ID = item['sub_ID']
	
	item['selected'] = True
	for items in options_items:
		if items != item:
			items['selected'] = False