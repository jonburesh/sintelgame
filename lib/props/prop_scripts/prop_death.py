'''
--------------------------------------------------------------------------------------------------------
prop has died :[
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import prop_scripts.prop_sound

def init(cont):
	own = cont.owner
	
	own['timer'] = 0
	own['hitable'] = False
	
	#cont.activate(enemy_scripts.enemy_sound.randSound('death'))
	
	cont.activate('obj_fade')

def main(cont):
	own = cont.owner

	if own['timer'] > 1.5:
		own.endObject()
		#logic.globalDict['player_engage_list'].remove(own)