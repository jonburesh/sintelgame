'''
--------------------------------------------------------------------------------------------------------
script that runs the levels functions
handles selecting levels
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render, events

def init():
	global cont, own, mouse_move, mouse_over, mouse_click, enter_key, up_key, down_key, back_key, right_click, resume, end_scene, send_mess, load_game
	cont = logic.getCurrentController()
	own = cont.owner
	
	mouse_move = own.sensors['mouse_move']
	mouse_over = own.sensors['mouse_over']
	mouse_click = own.sensors['mouse_click']
	right_click = own.sensors['right_click']
	enter_key = own.sensors['enter_key']
	back_key = own.sensors['back_key']
	up_key = own.sensors['up_key']
	down_key = own.sensors['down_key']
	
	end_scene = own.actuators['end_scene']
	resume = own.actuators['resume']
	send_mess = own.actuators['send_mess']
	load_game = own.actuators['load_game']
	
	#run once
	if own['sort_list'] != True:
		sortList()
		own['sort_list'] = True
		
def sortList():
	global levels_items, actual_levels_items, obj_list
	obj_list = logic.getCurrentScene().objects
	levels_items = []
	actual_levels_items = []
	lenght = len(logic.globalDict['menu_levels'])
	#print (logic.globalDict['menu_levels'])
	for ob in obj_list:
		if 'ID' in ob:
			levels_items.append(ob)
			#print (levels_items)
			
	for levels in levels_items:
		levels['able'] = True
		levels['text'] = logic.globalDict['menu_levels'][lenght-1]
		lenght -=1
		if lenght <0:
			lenght = 0
		try:
			actual_levels_items.append(levels)
			if levels == levels_items[own['level_count']-1]:
				break
		except:
			print ('too many levels in the level folder')
	
	for levels in levels_items:
		if levels['able'] != True:
			for i in levels.children:
				i.visible = 0
	
	actual_levels_items[0]['selected'] = True
	set_sel(actual_levels_items[0])
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
		cont.activate(end_scene)
		cont.activate(resume)
		cont.activate(send_mess)
		logic.OPTIONS_CURRENT_ID = 0
		
	if mouse_move.positive:
		own['mouse_timer'] +=1
		if own['mouse_timer'] >=15:
			own['mouse_movement'] = True
		
	if own['mouse_movement'] == True:
		if mouse_over.hitObject != None:
			OVER = mouse_over.hitObject.parent
			
			if 'selected' in OVER:
				if OVER['able'] == True:
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
	for items in actual_levels_items:
		if items['ID'] == ID:
			return items
	else:
		return False
		
def set_active(item):
	item['active'] = True
	logic.globalDict['Load_Next'] = item['text']
	print ('will load ',logic.globalDict['Load_Next'], 'next.')
	logic.saveGlobalDict()
	#cont.activate(load_game)
	cont.activate('fade_out')
				
def set_sel(item):
	logic.OPTIONS_CURRENT_ID = item['ID']
	#logic.OPTIONS_CURRENT_SUB_ID = item['sub_ID']
	
	item['selected'] = True
	for items in actual_levels_items:
		if items != item:
			items['selected'] = False