'''
--------------------------------------------------------------------------------------------------------
moves the enemy
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import enemy_scripts.enemy_sound

def main(cont):
	own = cont.owner
	
	hp_change = cont.sensors['hp_change']
	
	rig = own.children[own['type']+'_rig']
	
	if hp_change.positive:
		own.state = logic.KX_STATE4
		own['wait_time'] = 0
	
	if own['TRACK'] == 'FRONT':
		cont.activate('track_front')
	elif own['TRACK'] =='BACK':
		cont.activate('track_back')
	elif own['TRACK'] =='LEFT':
		cont.activate('track_left')
	elif own['TRACK'] =='RIGHT':
		cont.activate('track_right')

	rig.playAction(own['type']+'_walk2', 1, 34, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 5)
	try:
		cont.activate(enemy_scripts.enemy_sound.randSound('move'))
	except:
		pass
	
	if round(rig.getActionFrame(0)) == 15:
		#print ('THRUST')
		own.setLinearVelocity([0, (own['SPEED']), -9.8], True)

	if own['wait_time'] >=4:
		own.state = logic.KX_STATE16
