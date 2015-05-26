'''
--------------------------------------------------------------------------------------------------------
deals with player stats
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main():
	cont = logic.getCurrentController()
	own = cont.owner
	hp_changed = cont.sensors['hp_changed'].positive
	
	if hp_changed:
		if logic.globalDict['player_hp'] > own['hp']:
			#hp went down
			logic.sendMessage('hp_down')
			logic.globalDict['player_hp'] = own['hp']
		elif logic.globalDict['player_hp'] < own['hp']:
			#hp went down
			logic.sendMessage('hp_up')
			logic.globalDict['player_hp'] = own['hp']
def init():
	cont = logic.getCurrentController()
	own = cont.owner
	#if globalDict value does not exist, make one
	try:
		logic.globalDict['player_hp']
	except:
		logic.globalDict['player_hp'] = own['hp']