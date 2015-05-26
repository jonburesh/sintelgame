'''
--------------------------------------------------------------------------------------------------------
for hidden enemy types (takes the place of idle)
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from random import randint
import enemy_scripts.enemy_sound

def init(cont):
	own = cont.owner
	own['dig_time'] = 0
	
	rig = own.children[own['TYPE']+'_rig']

	
	rig.playAction(own['TYPE']+'_emerge', 1, 40, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)

def main(cont):
	own = cont.owner

	if own['dig_time'] >= 1.5:
		own.state = logic.KX_STATE3