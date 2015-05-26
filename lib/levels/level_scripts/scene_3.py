'''
--------------------------------------------------------------------------------------------------------
first gameplay
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main(cont):
	player = logic.getCurrentScene().objects['sintel_col']
	player['DREAM'] = True
	
	own = cont.owner
	cont.activate('blur')

def loop(cont):
	own = cont.owner
	trigger_1 = cont.sensors["trigger_1"].positive
	trigger_2 = cont.sensors["trigger_2"].positive
	trigger_3 = cont.sensors["trigger_3"].positive
	
	if own['current_dialog'] == 0:
		if trigger_1:
			own['current_dialog'] +=1
			own['go_dialog'] = True
			cont.activate('flare_1')
	elif own['current_dialog'] ==1:
		if trigger_2:
			own['current_dialog'] +=1
			own['go_dialog'] = True
			cont.activate('flare_2')
	elif own['current_dialog'] ==2:
		if trigger_3:
			own['current_dialog'] +=1
			own['go_dialog'] = True
			own.sendMessage('fade_out')