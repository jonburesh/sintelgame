'''
--------------------------------------------------------------------------------------------------------
stuns the enemy for a short time - plays hurt animation
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main(cont):
	own = cont.owner
	rig = own.children[own['TYPE']+'_rig']
	
	#disable collision
	own.suspendDynamics()
	#go under
	if own['dug'] == False:
		own['dig_time'] = 0
		rig.playAction(own['TYPE']+'_dig', 1, 100, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
		cont.activate('add_dig_fx')
		own['dug'] = True
		own['hitable'] = False
		#come back
	if own['dig_return'] == False:
		if round(rig.getActionFrame(0)) == 75:
			own.position[2] = own.position[2] - 1
	if own['dig_time'] >= 10 and own['dig_time'] < 10.1:
		if own['dug'] == True:
			if own['dig_return'] == False:
				own.position[2] = own.position[2] + 3
				own['dig_return'] = True
			else:
				rig.playAction(own['TYPE']+'_dig', 100, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
	elif own['dig_time'] >= 10.1:
		#back to battle
		if not rig.isPlayingAction(0):
			
			own.state = logic.KX_STATE2
			own['dug'] = False
			own['hitable'] = True
			own['dig_return'] = False
			own['dig_time'] = 0
			own.restoreDynamics()

def hide_init(cont):
	own = cont.owner
	rig = own.children[own['TYPE']+'_rig']
	
	own['dig_time'] = 0
	
	rig.playAction(own['TYPE']+'_emerge', 40, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
			
def hide(cont):
	own = cont.owner
	rig = own.children[own['TYPE']+'_rig']
	
	try:
		if rig.constraints['rock_rig:tracker'].enforce > 0:
			rig.constraints['rock_rig:tracker'].enforce -= .01
	except:
		rig.constraints['rock_rig:tracker'].enforce = 0
		
	
	if own['dig_time'] > 1:
		own.state = logic.KX_STATE2