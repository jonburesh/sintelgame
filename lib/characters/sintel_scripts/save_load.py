'''
--------------------------------------------------------------------------------------------------------
Saving and loading for sintel
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def save():
	#Start by saving the current level name
	try:
		LEVEL_MAIN = logic.getCurrentScene().objects['LEVEL_MAIN']
		logic.globalDict['level_name'] = LEVEL_MAIN['level_name']
		logic.globalDict['Load_Next'] = LEVEL_MAIN['level_name']
		#save all of the level's properties
		for prop in LEVEL_MAIN.getPropertyNames():
			logic.globalDict['LEVEL_MAIN',prop] = LEVEL_MAIN[prop]
			print (logic.globalDict['LEVEL_MAIN',prop])
	except:
		print ('LEVEL_MAIN not found. Current level will not be saved.')
		logic.globalDict['level_name'] = 'default'
	
	
	#Now for player information
	player = logic.getCurrentScene().objects['sintel_col']
	player_stats = logic.getCurrentScene().objects['player_stats']
	
	#position
	logic.globalDict['player_pos'] = list(player.worldPosition)
	logic.globalDict['player_ori'] = list(player.worldOrientation[0]),list(player.worldOrientation[1]),list(player.worldOrientation[2])

	#stats
	#logic.globalDict['player_lvl'] = player_stats['lvl']
	#logic.globalDict['player_max_hp'] = player_stats['mhp']
	#logic.globalDict['player_current_hp'] = player_stats['chp']
	logic.globalDict['player_hp'] = player_stats['hp']

	#Save
	logic.saveGlobalDict()
	#print('Saved Game')
	logic.globalDict['game_notifications'].append('Saved Game')

def load_game():
	load()
	logic.globalDict['game_load'] = True
	logic.saveGlobalDict()
	
	cont = logic.getCurrentController()
	own = cont.owner
	
	loading = cont.actuators['loading']
	cont.activate(loading)
	
def load():
	#Load
	logic.loadGlobalDict()
	#Now for player information
	player = logic.getCurrentScene().objects['sintel_col']
	player_stats = logic.getCurrentScene().objects['player_stats']
	#level props
	LEVEL_MAIN = logic.getCurrentScene().objects['LEVEL_MAIN']
	for prop in LEVEL_MAIN.getPropertyNames():
		LEVEL_MAIN[prop] = logic.globalDict['LEVEL_MAIN',prop]
	
	#position
	player.worldPosition = tuple(logic.globalDict['player_pos'])
	player.worldOrientation = tuple(logic.globalDict['player_ori'])
	
	#stats
	#player_stats['lvl'] = logic.globalDict['player_lvl']
	#player_stats['mhp'] = logic.globalDict['player_max_hp']
	#player_stats['chp'] = logic.globalDict['player_current_hp']
	player_stats['hp'] = logic.globalDict['player_hp']
	
	logic.globalDict['game_notifications'].append('Loaded Game')
	
def main():
	cont = logic.getCurrentController()
	own = cont.owner
	
	F5 = cont.sensors['F5'].positive
	F9 = cont.sensors['F9'].positive
	
	if F5:
		save()
	
	if F9:
		load_game()