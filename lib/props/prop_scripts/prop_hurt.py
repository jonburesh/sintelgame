'''
--------------------------------------------------------------------------------------------------------
prop has been hit
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import prop_scripts.prop_sound

def init(cont):
	own = cont.owner
	own['timer'] = 0
	
	#cont.activate('blood_spawn')
	#move us back a little
	threat = logic.globalDict[str(own)+'_threat']
	dir = (threat.worldPosition - own.worldPosition).normalized()
	#toss us in the opposite direction
	own.setLinearVelocity(-dir*5, False)
	#own.setLinearVelocity([0, -7, -9.8], True)

def main(cont):
	own = cont.owner
	
	if own['health'] <=0:
		own.state = logic.KX_STATE30

	if own['timer'] > .4:
		#back to idle
		own.state = logic.KX_STATE1
		#own.setLinearVelocity([0, 0, -9.8], True)