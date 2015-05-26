'''
--------------------------------------------------------------------------------------------------------
script that runs the options functions
handles selecting items
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render, events
from menu_scripts.options_save import save_settings

def init():
	global cont, own, obj_list, options_items, mouse_move, mouse_over, mouse_click, enter_key, up_key, down_key, all_keys, back_key, right_click
	cont = logic.getCurrentController()
	own = cont.owner

	obj_list = logic.getCurrentScene().objects

	options_items = []

	for ob in obj_list:
		if 'ID' in ob:
			options_items.append(ob)
			#print (options_items)
			
	mouse_move = own.sensors['mouse_move']
	mouse_over = own.sensors['mouse_over']
	mouse_click = own.sensors['mouse_click']
	right_click = own.sensors['right_click']
	enter_key = own.sensors['enter_key']
	back_key = own.sensors['back_key']
	up_key = own.sensors['up_key']
	down_key = own.sensors['down_key']
	all_keys = own.sensors['all_keys']
	
def setup():
	#logic.OPTIONS_CURRENT_SUB_ID = 0
	logic.OPTIONS_CURRENT_ID = 0
	render.showMouse(1)
	
def main():
	try:
		logic.OPTIONS_CURRENT_ID
	except:
		setup()
		
	init()
	if enter_key.positive:
		set_active(get_ID(logic.OPTIONS_CURRENT_ID))
		
	if back_key.positive or right_click.positive:
		obj_list['return_option']['active'] = True
		logic.OPTIONS_CURRENT_ID = 0
		
	if mouse_move.positive:
		own['mouse_timer'] +=1
		if own['mouse_timer'] >=15:
			own['mouse_movement'] = True
		
	if own['mouse_movement'] == True:
		if mouse_over.hitObject != None:
			OVER = mouse_over.hitObject.parent
			
			if 'selected' in OVER:
				set_sel(OVER)
			if mouse_click.positive:
				set_active(OVER)

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
	if item['type'] == 'choice':
		if item['option'] == '1024x768':
			item['option'] = '1024x1280'
		elif item['option'] == '1024x1280':
			item['option'] = '1280x768'
		elif item['option'] == '1280x768':
			item['option'] = '1280x800'
		elif item['option'] == '1280x800':
			item['option'] = '1280x1024'
		elif item['option'] == '1280x1024':
			item['option'] = '1440x900'
		elif item['option'] == '1440x900':
			item['option'] = '1600x900'
		elif item['option'] == '1600x900':
			item['option'] = '1600x1200'
		elif item['option'] == '1600x1200':
			item['option'] = '1680x1050'
		elif item['option'] == '1680x1050':
			item['option'] = '1920x1080'
		elif item['option'] == '1920x1080':
			item['option'] = '1920x1200'
		elif item['option'] == '1920x1200':
			item['option'] = '2560x1440'
		elif item['option'] == '2560x1440':
			item['option'] = '800x600'
		elif item['option'] == '800x600':
			item['option'] = '1024x768'
		else:
			item['option'] = '800x600'
	elif item['type'] == 'diff':
		if item['option'] =='Casual':
			item['option'] = 'Easy'
		elif item['option'] =='Easy':
			item['option'] = 'Normal'
		elif item['option'] =='Normal':
			item['option'] = 'Hard'
		elif item['option'] =='Hard':
			item['option'] = 'Casual'
	elif item['type'] == 'qual':
		if item['option'] =='Low':
			item['option'] = 'Medium'
		elif item['option'] =='Medium':
			item['option'] = 'High'
		elif item['option'] =='High':
			item['option'] = 'Low'
	elif item['type'] == 'number':
		if item['option'] !=3:
			item['option'] +=1
		else:
			item['option'] =1
	elif item['type'] == 'scale':
		if item['option'] =='Normal':
			item['option'] = 'Large'
		elif item['option'] =='Large':
			item['option'] = 'Small'
		elif item['option'] =='Small':
			item['option'] = 'Normal'
	elif item['type'] == 'bool':
		item['option'] = not item['option']
	if item['ID'] == 7 or item['ID'] == 8:
		logic.OPTIONS_CURRENT_ID = 0
	if item['ID'] ==8:
		save_settings()
	item['active'] = True
				
def set_sel(item):
	logic.OPTIONS_CURRENT_ID = item['ID']
	#logic.OPTIONS_CURRENT_SUB_ID = item['sub_ID']
	
	item['selected'] = True
	for items in options_items:
		if items != item:
			items['selected'] = False