'''
--------------------------------------------------------------------------------------------------------
script that runs the menu functions
handles selecting items
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render
from menu_scripts import set_defualt_vars

cont = logic.getCurrentController()
own = cont.owner

print ('uiawfuijhfhjgfwuijkhfwelhjkfwehjgl')
obj_list = logic.getCurrentScene().objects

menu_items = []

for ob in obj_list:
	if 'ID' in ob:
		menu_items.append(ob)
		#print (menu_items)
		
def test_save():
	try:
		logic.loadGlobalDict()
		logic.globalDict['player_pos']
		print ('found save')
		return True
	except:
		set_defualt_vars.main()
		return False	
		
resume_game = logic.getCurrentScene().objects['resume_option']

if test_save():
	print ('Found Save File')
	resume_game['next_level'] = logic.globalDict['Load_Next']
else:
	#no acceptable save file found, remove resume menu option
	
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
		logic.saveGlobalDict()
	if item['ID'] == 0:
		logic.globalDict['game_load'] = True
		logic.globalDict['Load_Next'] = logic.globalDict['level_name']
		print ('setting loading file to:',logic.globalDict['Load_Next'])
		logic.saveGlobalDict()
	
def set_sel(item):
	logic.MENU_CURRENT_ID = item['ID']
	logic.MENU_CURRENT_SUB_ID = item['sub_ID']
	
	item['selected'] = True
	for items in menu_items:
		if items != item:
			items['selected'] = False