'''
--------------------------------------------------------------------------------------------------------
randomly move around, then go back to idle
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import random

def init(cont):
	own = cont.owner
	
	#set a timer
	own['dig_time'] = 0
	#choose left or right
	own['move_dir'] = random.choice(['left','right','forward'])

def main(cont):
	own = cont.owner
	rig = own.children[own['TYPE']+'_rig']
	
	if own['move_dir'] == 'left':
		own.setAngularVelocity([0, 0, 1], False)
	elif own['move_dir'] == 'right':
		own.setAngularVelocity([0, 0, -1], False)
	elif own['move_dir'] == 'forward':
		#check if anything is in front of us
		from_pos = own.position

		to_pos = from_pos[:]
		to_pos = [from_pos[0], from_pos[1] -6, from_pos[2]]

		front_ray = own.rayCast(to_pos, from_pos, 5, "wall")
		#something is infront, turn
		if front_ray[0]:
			own['move_dir'] = random.choice(['left','right'])
		#nothing infront, move forward
		else:
			if own['TYPE']=='snail':
				if round(rig.getActionFrame(0)) == 8:
					own.setLinearVelocity([0, (own['SPEED']) /2, 0], True)
			else:	
				vel = own.getLinearVelocity(True)
				own.setLinearVelocity([0, own['SPEED'] /2, vel[2]], True)
	else:
		print ('something went wrong...')
	
	if own['move_dir'] == 'forward' or own['TYPE'] == 'snail':
		move_act = rig.actuators[own['TYPE']+'_move']
		end_frame = move_act.frameEnd
		rig.playAction(own['TYPE']+'_move', 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 5)
	else:
		move_act = rig.actuators[own['TYPE']+'_move_'+own['move_dir']]
		end_frame = move_act.frameEnd
		rig.playAction(own['TYPE']+'_move_'+own['move_dir'], 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 5)
	
	if round(rig.getActionFrame(0)) == end_frame:
		own.setAngularVelocity([0, 0, 0], False)
		#own.setLinearVelocity([0, 0, 0], False)
		own.state = logic.KX_STATE2