'''
--------------------------------------------------------------------------------------------------------
saves the global dictionary variables to defualt values
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main(new_game):
	#print ('setting defualt vars')
	logic.globalDict['game_load'] = False
	logic.globalDict['player_pos'] = None
	logic.globalDict['player_ori'] = None
	logic.globalDict['player_hp'] = 100
	logic.globalDict['game_notifications'] = []
	logic.globalDict['game_last_notification'] = ''
	logic.globalDict['game_objective'] = 'test'
	logic.globalDict['sintel_0_threat'] = []
	logic.globalDict['target'] = None
	logic.globalDict['game_dialog'] = []
	logic.globalDict['menu_levels'] = []
	logic.globalDict['level_name'] = None
	'''
	logic.globalDict['cfg_post'] = None
	logic.globalDict['cfg_UI'] = None
	logic.globalDict['cfg_difficulty'] = None
	logic.globalDict['cfg_LOD'] = None
	'''
	if new_game == False:
		logic.globalDict['Load_Next'] = None
		
	logic.saveGlobalDict()