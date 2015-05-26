from bge import logic
from random import randint
import enemy_scripts.enemy_sound


def main(cont):
	own = cont.owner
	
	#get the rig
	rig = own.children[own['TYPE']+'_rig']
	#tracker = own.sensors['tracker'].owner
	tracker = logic.getCurrentScene().objects['rock_snake_tracker']

	threat = logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'][0]
	if not own in logic.globalDict[threat['TYPE']+ '_' + str(threat['ID']) + '_threat']:
		logic.globalDict[threat['TYPE']+ '_' + str(threat['ID']) + '_threat'].append(own)
		
	#enemy_track.object = threat
	
	tracker.position = threat.position
	#rig.constraints['rock_rig:tracker'].active = True
	if rig.constraints['rock_rig:tracker'].enforce < .5:
		rig.constraints['rock_rig:tracker'].enforce += .01
	
	if threat != None:
		dist = own.getDistanceTo(threat)
	else:
		own.state = logic.KX_STATE16
	
	rig.playAction(own['TYPE']+'_idle', 1, 119, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 5)
	#in attack range
	if dist <=8:
		if own['dig_time'] > 1:
			own.state = logic.KX_STATE18
			own['dig_time'] = 0
			#cont.activate(enemy_scripts.enemy_sound.randSound('growl'))
	if dist >= 20:
		own.state = logic.KX_STATE16
		#rig.constraints['rock_rig:tracker'].active = False
		#rig.constraints['rock_rig:tracker'].enforce = 0