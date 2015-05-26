'''
--------------------------------------------------------------------------------------------------------
waits for enemy to stop moving
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main():
	cont = logic.getCurrentController()
	own = cont.owner
	
	hp_change = cont.sensors['hp_change']
	
	if hp_change.positive:
		cont.activate('hurt_state')
		own['wait_time'] = 0
	
	for ob in own.children:
		name = ob.name
		if 'snail_rig' in name:
			if not ob.isPlayingAction(0):
				ob.stopAction(1)
				ob.stopAction(2)
				ob.playAction('snail_idle', 1, 220, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 5)
			
	speed = own.getLinearVelocity()
	if speed[0] == 0 and speed[1] == 0 and speed[2] ==0:
		if own['wait_time'] >=1:
			cont.activate('main_state')