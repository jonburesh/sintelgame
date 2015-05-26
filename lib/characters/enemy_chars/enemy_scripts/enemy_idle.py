from bge import logic
from random import randint
import enemy_scripts.enemy_sound


def main(cont):
	own = cont.owner
	
	threat_near = cont.sensors['threat_near']
	
	#get the rig
	rig = own.children[own['TYPE']+'_rig']
	
	threat_near.distance = own['THREAT_DIST'] 

	#when idle don't move
	if not 'HOVER' in own:
		own.setLinearVelocity([0, 0, -9.8], True)
	else:
		vel = own.getLinearVelocity(True)
		own.setLinearVelocity([0, 0, vel[2]], True)
	
	if threat_near.positive:
		#threat detected
		print ("Threat detected from",own['TYPE'],own['ID'])
		#threat = threat_near.hitObject
		#if this threat isnt already known, add it to the list
		for threat in threat_near.hitObjectList:
			if not threat in logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat']:
				logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'].append(threat)
		own.state = logic.KX_STATE3
		try:
			cont.activate(enemy_scripts.enemy_sound.randSound('growl'))
		except:
			pass
	if own['BUSY'] != True:
		#get a random number between 1 & 500. higher the number, the less activity
		IDLE_TIME = randint(1, 500)
		#randomly move around
		if IDLE_TIME == 40:
			own.state = logic.KX_STATE17
		#growl
		if IDLE_TIME == 30:
			shake_act = rig.actuators[own['TYPE']+'_shake']
			end_frame = shake_act.frameEnd
			rig.playAction(own['TYPE']+'_shake', 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
			#cont.activate(enemy_scripts.enemy_sound.randSound('growl'))
			print ('growling')
			#set busy so it can't growl while growling
			own['BUSY'] = True

		#idle animation
		else:
			idle_act = rig.actuators[own['TYPE']+'_idle']
			end_frame = idle_act.frameEnd
			rig.playAction(own['TYPE']+'_idle', 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 5)
	else:
		#not doing anything
		if not rig.isPlayingAction(0):
			own['BUSY'] = False