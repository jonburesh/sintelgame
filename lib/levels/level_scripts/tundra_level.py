'''
tundra level script
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

player = logic.getCurrentScene().objects['sintel_col']


def init(cont):
	
	#turn on the hud
	logic.sendMessage('HUD_on')
	#give player the torch
	player['torch'] = True
	
def main(cont):
	own = cont.owner
	
	if own['current_dialog'] == 0:
		own['go_dialog'] = True
		own['current_dialog'] += 1
	elif own['current_dialog'] == 1:
		own['go_dialog'] = True
		own['current_dialog'] += 1
	elif own['current_dialog'] == 2:
		own['go_dialog'] = True
		own['current_dialog'] += 1