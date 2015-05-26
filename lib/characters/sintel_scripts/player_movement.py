'''
--------------------------------------------------------------------------------------------------------
responsible for moving sintel
handles movement animations
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from random import *

ACCEL_RATE = .2
GRAV = -9.8
MAX_ROT = 3

scene = logic.getCurrentScene()

sintel_rig = scene.objects['sintel_rig']
target_dir = scene.objects['target_dir']
sintel_col = scene.objects['sintel_col']

BLENDIN = 5

def RanSounds(type):
	swish = ['swish_complex2', 'swish_complex', 'swish_simple', 'swish_simple_3']
	action = ''
	if type ==1:
		action = choice(swish)
	else:
		print ("Unexpected value: %i" % type)
	return action

def main(cont):
	own = cont.owner

	global BLENDIN
	
	movement_track = own.actuators['movement_track']
	front_track = own.actuators['front_track']
	back_track = own.actuators['back_track']
	left_track = own.actuators['left_track']
	right_track = own.actuators['right_track']
	track_f_right = own.actuators['track_f_right']
	track_f_left = own.actuators['track_f_left']
	track_b_right = own.actuators['track_b_right']
	track_b_left = own.actuators['track_b_left']
	stuck_ray = own.sensors['stuck_ray']
	
	#can't go over max speed
	if own['RUN_SPEED'] > own['SPEED']:
		own['RUN_SPEED'] = own['SPEED']
		
	if own['RUN_SPEED'] < 0:
		own['RUN_SPEED'] = 0
	'''
	if own['floor_angle'] > 30:
		own.state = logic.KX_STATE4
	'''
	if own['FORWARD'] and own['LEFT']:
		cont.deactivate(front_track)
		cont.deactivate(back_track)
		cont.deactivate(left_track)
		cont.deactivate(right_track)
		cont.activate(track_f_left)
		cont.deactivate(track_f_right)
		cont.deactivate(track_b_right)
		cont.deactivate(track_b_left)
		target_dir['direction'] = 8
	elif own['FORWARD'] and own['RIGHT']:
		cont.deactivate(front_track)
		cont.deactivate(back_track)
		cont.deactivate(left_track)
		cont.deactivate(right_track)
		cont.deactivate(track_f_left)
		cont.activate(track_f_right)
		cont.deactivate(track_b_right)
		cont.deactivate(track_b_left)
		target_dir['direction'] = 2
	elif own['FORWARD']:
		cont.activate(front_track)
		cont.deactivate(back_track)
		cont.deactivate(left_track)
		cont.deactivate(right_track)
		cont.deactivate(track_f_left)
		cont.deactivate(track_f_right)
		cont.deactivate(track_b_right)
		cont.deactivate(track_b_left)
		target_dir['direction'] = 1
	elif own['BACK'] and own['LEFT']:
		cont.deactivate(front_track)
		cont.deactivate(back_track)
		cont.deactivate(left_track)
		cont.deactivate(right_track)
		cont.deactivate(track_f_left)
		cont.deactivate(track_f_right)
		cont.deactivate(track_b_right)
		cont.activate(track_b_left)
		target_dir['direction'] = 6
	elif own['BACK'] and own['RIGHT']:
		cont.deactivate(front_track)
		cont.deactivate(back_track)
		cont.deactivate(left_track)
		cont.deactivate(right_track)
		cont.deactivate(track_f_left)
		cont.deactivate(track_f_right)
		cont.activate(track_b_right)
		cont.deactivate(track_b_left)
		target_dir['direction'] = 4
	elif own['BACK']:
		cont.deactivate(front_track)
		cont.activate(back_track)
		cont.deactivate(left_track)
		cont.deactivate(right_track)
		cont.deactivate(track_f_left)
		cont.deactivate(track_f_right)
		cont.deactivate(track_b_right)
		cont.deactivate(track_b_left)
		target_dir['direction'] = 5
	elif own['LEFT']:
		cont.deactivate(front_track)
		cont.deactivate(back_track)
		cont.activate(left_track)
		cont.deactivate(right_track)
		cont.deactivate(track_f_left)
		cont.deactivate(track_f_right)
		cont.deactivate(track_b_right)
		cont.deactivate(track_b_left)
		target_dir['direction'] = 7
	elif own['RIGHT']:
		cont.deactivate(front_track)
		cont.deactivate(back_track)
		cont.deactivate(left_track)
		cont.activate(right_track)
		cont.deactivate(track_f_left)
		cont.deactivate(track_f_right)
		cont.deactivate(track_b_right)
		cont.deactivate(track_b_left)
		target_dir['direction'] = 3
	
	#no keys are being pressed, stop moving
	if not own['FORWARD'] and not own['BACK'] and not own['RIGHT'] and not own['LEFT']:
		own['MOVE'] = False
	else:
		own['MOVE'] = True
		
	if own['MOVE']:
		#turn off dynamic foot placement
		sintel_rig.state = logic.KX_STATE1
		#check to make sure we are not stuck
		if not stuck_ray.positive:
			own['MOVING'] = True
		#move us
		own.setLinearVelocity([0, own['RUN_SPEED'], GRAV], True)
		#smoothness
		if own['RUN_SPEED'] != own['SPEED']:
			own['RUN_SPEED'] += ACCEL_RATE * 1.5
		
		if own['RUN'] == True and own['ENABLE_RUN'] == True:
			own['RUNNING'] = True
		else:
			own['RUNNING'] = False
		
		if own['RUNNING'] == True and own['MOVING'] == True:
			own['SPEED'] = own['MAX_SPEED']
			if own['MOVE_TIME'] > 1:
				#movement_track.time = 25
				front_track.time = 25
				left_track.time = 25
				right_track.time = 25
				back_track.time = 25
				track_f_left.time = 25
				track_f_right.time = 25
				track_b_right.time = 25
				track_b_left.time = 25
			else:
				time = 10
				front_track.time = time
				left_track.time = time
				right_track.time = time
				back_track.time = time
				track_f_left.time = time
				track_f_right.time = time
				track_b_right.time = time
				track_b_left.time = time
			#play run cycle
			sintel_rig.playAction('sintel_run_staff', 1, 21, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = own['ANIM_SPEED'], blendin = 5)
		else:
			own['SPEED'] = own['WALK_SPEED']
			if own['MOVE_TIME'] > 1:
				time = 15
				front_track.time = time
				left_track.time = time
				right_track.time = time
				back_track.time = time
				track_f_left.time = time
				track_f_right.time = time
				track_b_right.time = time
				track_b_left.time = time
			else:
				time = 10
				front_track.time = time
				left_track.time = time
				right_track.time = time
				back_track.time = time
				track_f_left.time = time
				track_f_right.time =time
				track_b_right.time = time
				track_b_left.time = time
			#play walk cycle
			if own['MOVING'] == True:
				sintel_rig.playAction('sintel_run_staff', 1, 21, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = (own['ANIM_SPEED'] *.6), blendin = 5)
				#there is a problem with a driver making the walk animation all funky in game
				#sintel_rig.playAction('sintel_walk', 1, 29, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = (own['ANIM_SPEED'] * .6), blendin = BLENDIN/2)
			
	if own['MOVE'] != True:
		set_idle()
		own['MOVING'] = False
		own['RUNNING'] = False
		cont.deactivate(front_track)
		cont.deactivate(back_track)
		cont.deactivate(left_track)
		cont.deactivate(right_track)
		cont.deactivate(track_f_left)
		cont.deactivate(track_f_right)
		cont.deactivate(track_b_right)
		cont.deactivate(track_b_left)
		
		if own['RUN_SPEED'] > 0:
			own['RUN_SPEED'] -= (ACCEL_RATE *3)
			own.setLinearVelocity([0, own['RUN_SPEED'], GRAV], True)
		
	if own['CLICK'] and own['ENABLE_ATK'] == True:
		own['COMBAT'] = True
		own['COMBAT_TIME'] = 0
		own.state = logic.KX_STATE3
		#cont.activate(RanSounds(1))
		#set attack state 
		sintel_rig.state = logic.KX_STATE1
		own['CLICK'] = False
		own['MOVING'] = False
		own['RUNNING'] = False
		own['MOVE'] = False
		own['RUN_SPEED'] = 0
		#stop moving
		own.setLinearVelocity([0, 0, GRAV], True)
		time = 10
		front_track.time = time
		left_track.time = time
		right_track.time = time
		back_track.time = time
		track_f_left.time = time
		track_f_right.time = time
		track_b_right.time = time
		track_b_left.time =time
			
	#reset combo chain
	if own['COMBO_TIME'] > 1.5:
		own['ATK_COMBO'] = 0
		own['COMBO_TIME'] = 0
		
	#player is walking into a wall
	if stuck_ray.positive:
		own['SPEED'] = 0
		own['MOVING'] = False
		set_idle()
		
	if own['COMBAT'] == True:
		if own['COMBAT_TIME'] > 4:
			try:
				if logic.globalDict[own['TYPE']+ '_' + str(own['ID']) +'_threat'] == []:
					own['COMBAT'] = False
					print (logic.globalDict[own['TYPE']+ '_' + str(own['ID']) +'_threat'])
			except:
				own['COMBAT'] = False

def set_idle():
	global BLENDIN
	if sintel_rig.state == logic.KX_STATE1:
		if sintel_col['COMBAT'] == True:
			sintel_rig.playAction('sintel_idle_attack_2', 1, 39, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = sintel_col['ANIM_SPEED'], blendin = 10)
		else:
			sintel_rig.playAction('sintel_idle', 1, 30, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = sintel_col['ANIM_SPEED'], blendin = 10)
		#after 15 frames, activate dynamic foot placement
			if round(sintel_rig.getActionFrame(0)) == 10:
				sintel_rig.state = logic.KX_STATE2
	#play idle animation for dynamic foot placement
	elif sintel_rig.state == logic.KX_STATE2:
		sintel_rig.playAction('sintel_idle_no_feet', 30, 219, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = sintel_col['ANIM_SPEED'], blendin = 10)

#check if player is on the ground
def ground_check(cont):
	own = cont.owner
	ground_ray = cont.sensors['ground_ray']
	#check it see if we aren't on the ground
	if not ground_ray.positive and sintel_col.state != logic.KX_STATE16:
		#fall state
		sintel_col.state = logic.KX_STATE17
		own.state = logic.KX_STATE2
		print ('falling state')

#check if the player has landed
def land_check(cont):
	own = cont.owner
	ground_ray = cont.sensors['ground_ray']
	if ground_ray.positive:
		sintel_col.state = logic.KX_STATE18
		own.state = logic.KX_STATE1
		scene.addObject('knockback', 'sintel', 5)
		print ('landed state')
		
#player is falling in mid air
def player_fall(cont):
	own = cont.owner
	
	sintel_rig.state = logic.KX_STATE1
	own['RUN_SPEED'] = 0
	own['MOVE'] = False
	own['SPEED'] = 0
	own['MOVING'] = False
	
	own.setLinearVelocity([0, 10, -25], True)
	sintel_rig.playAction('sintel_fall', 1, 39, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = own['ANIM_SPEED'], blendin = 5)

#player has landed
def player_land(cont):
	own = cont.owner
	global BLENDIN
	own['land_time'] +=1
	own.setLinearVelocity([0, 0, -25], True)
	sintel_rig.playAction('sintel_land', 1, 15, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = own['ANIM_SPEED'], blendin = 5)
	cont.activate('fall_sound')
	BLENDIN = 25
	own['ATK_PLAY'] = False
	own['COMBO_FINISH'] = False
	own['dmg_done'] = False
	if own['land_time'] >= 30:
		own.state = logic.KX_STATE1
		own['land_tine'] = 0