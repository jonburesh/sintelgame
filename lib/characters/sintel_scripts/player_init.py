'''
--------------------------------------------------------------------------------------------------------
starts the player
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render
from sintel_scripts.save_load import load

def main(cont):
	own = cont.owner
	render.showMouse(0)
	'''
	try:
		ID = logic.globalDict['ID'] = logic.globalDict['ID'] + 1
	except:
		ID = logic.globalDict['ID'] = 0
	'''
	own['ID'] = 0
	
	if own['DREAM'] == True:
		own['ANIM_SPEED'] = .5
		own['MAX_SPEED'] = 10
		own['ENABLE_ATK'] = False
		own['RUNNING'] = True
		own['RUN'] = True
	else:
		own['ANIM_SPEED'] = 1
		own['MAX_SPEED'] = 25
		own['ENABLE_ATK'] = True
		own['ENABLE_RUN'] = True
	
	init_load()
	
def init_load():
	try:
		logic.loadGlobalDict()
		#found a save but we are not loading it - overwrite
		if logic.globalDict['game_load'] == False:
			init_create_vars()
		#loading save
		else:
			load()
			logic.globalDict['game_load'] = False
			logic.saveGlobalDict()
			start_game()
	#no save found
	except:
		print ('game_load var not found')
		init_create_vars()

def init_create_vars():
	print ('creating new vars')
	own = logic.getCurrentController().owner
	logic.globalDict['ID'] = 0
	logic.globalDict['game_load'] = False
	logic.globalDict['player_pos'] = None
	logic.globalDict['player_ori'] = None
	logic.globalDict['player_hp'] = 100
	logic.globalDict['game_notifications'] = []
	logic.globalDict['game_last_notification'] = ''
	logic.globalDict['game_objective'] = ''
	logic.globalDict['sintel_0_threat'] = []
	logic.saveGlobalDict()
	start_game()

def start_game():
	cont = logic.getCurrentController()
	own = cont.owner
	own.state = logic.KX_STATE1