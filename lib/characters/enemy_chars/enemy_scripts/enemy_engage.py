'''
--------------------------------------------------------------------------------------------------------
engage the threat
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import enemy_scripts.enemy_sound

SNAIL_DIST = 55

def main(cont):
	own = cont.owner
	
	enemy_track = cont.actuators['enemy_track']
	
	rig = own.children[own['TYPE']+'_rig']
	
	'''
	if own['TYPE'] == 'snail':
		threat_near.distance = SNAIL_DIST
	else:
		pass
	'''
	threat = logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'][0]
	if not own in logic.globalDict[threat['TYPE']+ '_' + str(threat['ID']) + '_threat']:
		logic.globalDict[threat['TYPE']+ '_' + str(threat['ID']) + '_threat'].append(own)
		
	enemy_track.object = threat
	
	if threat != None:
		dist = own.getDistanceTo(threat)
	else:
		own.state = logic.KX_STATE2
	#threat is not too far away, move closer
	if dist <= SNAIL_DIST and dist > 5.5:
		cont.activate(enemy_track)
		#play animation
		move_act = rig.actuators[own['TYPE']+'_move']
		end_frame = move_act.frameEnd
		rig.playAction(own['TYPE']+'_move', 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 5)
		try:
			cont.activate(enemy_scripts.enemy_sound.randSound('move'))
		except:
			pass
		#move us
		if own['TYPE']=='snail':
				if round(rig.getActionFrame(0)) == 15:
					own.setLinearVelocity([0,own['SPEED'], -9.8] , True)
		else:
			vel = own.getLinearVelocity(True)
			own.setLinearVelocity([0, own['SPEED'], vel[2]], True)
	#in attacking range
	if dist <=5.5:
		idle_act = rig.actuators[own['TYPE']+'_idle']
		end_frame = idle_act.frameEnd
		rig.playAction(own['TYPE']+'_idle', 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 5)
		cont.activate(enemy_track)
		if own['dig_time'] > 1:
			if own['TYPE']=='snail':
				if round(rig.getActionFrame(0)) == 15:
					own.setLinearVelocity([0,own['SPEED'], -9.8] , True)
			else:
				own.setLinearVelocity([0,own['SPEED'], 0] , True)
			own.state = logic.KX_STATE18
			own['dig_time'] = 0
			try:
				cont.activate(enemy_scripts.enemy_sound.randSound('growl'))
			except:
				pass
	#out of range, back to idle
	if dist >= SNAIL_DIST:
		cont.deactivate(enemy_track)
		own.state = logic.KX_STATE2
		print (logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'])
		logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'].remove(threat)
		logic.globalDict[threat['TYPE']+ '_' + str(threat['ID']) + '_threat'].remove(own)
		