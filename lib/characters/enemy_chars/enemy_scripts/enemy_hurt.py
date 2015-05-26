'''
--------------------------------------------------------------------------------------------------------
stuns the enemy for a short time - plays hurt animation
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import enemy_scripts.enemy_sound

def init(cont):
	own = cont.owner
	
	own['dig_time'] = 0
	
	rig = own.children[own['TYPE']+'_rig']
	hurt_act = rig.actuators[own['TYPE']+'_hurt']
	end_frame = hurt_act.frameEnd
	rig.playAction(own['TYPE']+'_hurt', 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
	#play a sound, add snail blood
	try:
		cont.activate(enemy_scripts.enemy_sound.randSound('hurt'))
	except:
		pass
	cont.activate('blood_spawn')
	#move us back a little
	threat = logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'][0]
	dir = (threat.worldPosition - own.worldPosition).normalized()
	#toss us in the opposite direction
	own.setLinearVelocity(-dir*4, False)
	#own.setLinearVelocity([0, -7, -9.8], True)

def main(cont):
	own = cont.owner
	
	if own['health'] <=0:
		own.state = logic.KX_STATE30

	if own['dig_time'] > .4:
		#back to combat
		own.state = logic.KX_STATE3
		own['hitable'] = True
		print ('back')
		#own.setLinearVelocity([0, 0, -9.8], True)