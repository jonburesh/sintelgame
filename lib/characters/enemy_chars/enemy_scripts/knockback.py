'''
--------------------------------------------------------------------------------------------------------
sends'em flying
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import enemy_scripts.enemy_sound
import mathutils

def init(cont):
	own = cont.owner
	#get the direction of the attacker
	threat = logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'][0]
	dir = (threat.worldPosition - own.worldPosition).normalized()
	#toss us in the opposite direction
	own.setLinearVelocity(-dir*30, False)
	
	rig = own.children[own['TYPE']+'_rig']
	hurt_act = rig.actuators[own['TYPE']+'_hurt']
	end_frame = hurt_act.frameEnd
	rig.playAction(own['TYPE']+'_hurt', 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
	
	own['dig_time'] = 0
	try:
		cont.activate(enemy_scripts.enemy_sound.randSound('hurt'))
	except:
		pass
	cont.activate('blood_spawn')

def main(cont):
	own = cont.owner
	
	#dead
	if own['health'] <=0:
		own.state = logic.KX_STATE30
	#not dead
	elif own['dig_time'] > 1.25:
		own['hitable'] = True
		own.state = logic.KX_STATE3