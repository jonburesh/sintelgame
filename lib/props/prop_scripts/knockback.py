'''
--------------------------------------------------------------------------------------------------------
sends'em flying
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import prop_scripts.prop_sound
import mathutils

def init(cont):
	own = cont.owner
	#get the direction of the attacker
	threat = logic.globalDict[str(own)+'_threat']
	dir = (threat.worldPosition - own.worldPosition).normalized()
	#toss us in the opposite direction
	own.setLinearVelocity(-dir*15, False)
	
	own['timer'] = 0
	#cont.activate(enemy_scripts.enemy_sound.randSound('hurt'))
	#cont.activate('blood_spawn')

def main(cont):
	own = cont.owner
	
	#dead
	if own['health'] <=0:
		own.state = logic.KX_STATE30
	#not dead
	elif own['timer'] > 1.25:
		#own.setLinearVelocity([0, 0, -9.8], True)
		own.state = logic.KX_STATE1