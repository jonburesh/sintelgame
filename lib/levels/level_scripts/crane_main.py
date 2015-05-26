from bge import logic

logic.crane_crate = None
player = logic.getCurrentScene().objects['sintel_col']

def init(cont):
	own = cont.owner
	
	if own['used_crane'] == False and logic.globalDict['crane_go'] == True:
		print ('starting crane')
		
		#set crane cam
		crane_cam = cont.sensors['crane_cam'].owner
		crane_head = cont.sensors['crane_head'].owner
		ship_target = cont.sensors['ship_target'].owner
		scene = logic.getCurrentScene()
		scene.active_camera = crane_cam
		#freeze player
		logic.sendMessage('player_freeze')
		logic.sendMessage('HUD_off')
		#send message
		logic.sendMessage('crane')
		#set player position
		player.position = own.position
		player.orientation = own.orientation
		#start crane
		cont.activate('crane_cam_rot')
		own['using_crane'] = True
		own.state = logic.KX_STATE1
		crane_head.state = logic.KX_STATE2
		ship_target.state = logic.KX_STATE2
	else:
		own.state = logic.KX_STATE2

def over(cont):
	crane_main = cont.sensors['crane_main'].owner
	if crane_main['using_crane'] == True:
		crane_main['crane_over'] = True
		print ('crane is done')
	
def main(cont):
	own = cont.owner
	
	crane_grab = cont.sensors['crane_grab'].owner
	crane_head = cont.sensors['crane_head'].owner
	crate_pos = cont.sensors['crate_pos'].owner
	
	space_key = cont.sensors['space_key']
	left_button = cont.sensors['left_button']
	crane_arm_col = cont.sensors['crane_arm_col']
	
	if own['crane_over'] == True:
		own['used_crane'] = True
		own['using_crane'] = False
		crane_head.state = logic.KX_STATE16
		own.state = logic.KX_STATE2
		player.position = own.position
		player.orientation = own.orientation
	
	if own['got_crate'] == False:
		if space_key.positive or left_button.positive:
			crane_grab.state = logic.KX_STATE2
			crane_head.state = logic.KX_STATE16
		if crane_arm_col.positive and crane_grab['crane_arm'] != 0:
			logic.crane_crate = crane_arm_col.hitObject
			logic.crane_crate.suspendDynamics()
			logic.crane_crate.setParent(crate_pos)
			logic.crane_crate.worldPosition = crate_pos.worldPosition
			own['got_crate'] = True
			crane_grab['crane_arm'] = 100
	else:
		if space_key.positive or left_button.positive:
			own['got_crate'] = False
			release()
			
		if 'food_crate' in logic.crane_crate and crane_grab['crane_arm'] == 0:
			crane_head.state = logic.KX_STATE3
			own.state = logic.KX_STATE3
			#store last rotation
			crane_angle = crane_head.localOrientation.to_euler()
			crane_head['last_rot'] = crane_angle[2]
			#print ('got the crate')
	
def release():
	logic.crane_crate.removeParent()
	logic.crane_crate.restoreDynamics()
	logic.crane_crate = None
	try:
		LEVEL_MAIN = logic.getCurrentScene().objects['LEVEL_MAIN']
		LEVEL_MAIN['got_crates'] += 1
	except:
		pass
	print ('releasing')

def got_crate(cont):
	own = cont.owner

	crane_angle = own.localOrientation.to_euler()
	
	cranezrot = cont.actuators['cranezrot']
	gear_rot = cont.actuators['gear_rot']
	gear_s_rot = cont.actuators['gear_s_rot']
	crane_move = cont.actuators['crane_move']
	
	crane_tip = cont.sensors['crane_tip'].owner
	crane_main = cont.sensors['crane_main'].owner
	
	
	if crane_tip.localPosition[0] < -9:
		crane_move.dLoc =(.1, 0, 0)
		cont.activate(crane_move)
	else:
		cont.deactivate(crane_move)
	
	if crane_angle[2] >= (own['start_rot']  - 1.3):
		cranezrot.dRot =(0, 0, -.01)
		gear_rot.dRot =(0, 0, .04)
		gear_s_rot.dRot =(0, .04, 0)

		cont.activate(gear_rot)
		cont.activate(gear_s_rot)
		cont.activate(cranezrot)
	else:
		cont.deactivate(gear_rot)
		cont.deactivate(gear_s_rot)
		cont.deactivate(cranezrot)
		own.state = logic.KX_STATE4
		own['got_crates'] +=1

def return_crane(cont):
	own = cont.owner
	
	crane_main = cont.sensors['crane_main'].owner
	crane_tip = cont.sensors['crane_tip'].owner
	
	if crane_main['crane_over'] == True:
		crane_main['used_crane'] = True
		crane_main['using_crane'] = False
		own.state = logic.KX_STATE16
		crane_main.state = logic.KX_STATE2
		player.position = crane_main.position
		player.orientation = crane_main.orientation
	
	mousemove = cont.sensors['mousemove'].positive
	#over_mess = cont.sensors['over_mess'].positive
	
	crane_main['got_crate'] = False
	
	crane_angle = own.localOrientation.to_euler()
	
	cranezrot = cont.actuators['cranezrot']
	gear_rot = cont.actuators['gear_rot']
	gear_s_rot = cont.actuators['gear_s_rot']

	if mousemove:
		own['mouse_timer'] +=1
		if own['mouse_timer'] >=5:
			own['mouse_movement'] = True
	
	if own['mouse_movement'] == True or crane_angle[2] >= (own['last_rot']):
		own['mouse_timer'] = 0
		own['mouse_movement'] = False
		cont.deactivate(gear_rot)
		cont.deactivate(gear_s_rot)
		cont.deactivate(cranezrot)
		own.state = logic.KX_STATE2
		crane_main.state = logic.KX_STATE1
	else:
		cranezrot.dRot =(0, 0, .01)
		gear_rot.dRot =(0, 0, .04)
		gear_s_rot.dRot =( 0, .04, 0)

		cont.activate(gear_rot)
		cont.activate(gear_s_rot)
		cont.activate(cranezrot)
		
def grab(cont):
	own = cont.owner
	
	crane_empty = cont.sensors['crane_empty'].owner
	crane_ref = cont.sensors['crane_ref'].owner
	crane_head = cont.sensors['crane_head'].owner
	
	own['crane_arm'] +=1
	
	if crane_empty['got_crate'] == True:
		if own.position[2] >= crane_ref.position[2]:
			own['crane_arm'] =200
			own.position[2] = crane_ref.position[2]
			
	if own['crane_arm'] >=100 and own['crane_arm'] < 200:
		cont.activate('retract')
		cont.activate('grab_gear_down')
		cont.deactivate('grab_motion')
		cont.deactivate('grab_gear_up')
	elif own['crane_arm'] >=200:
		cont.deactivate('retract')
		cont.deactivate('grab_motion')
		cont.deactivate('grab_gear_up')
		cont.deactivate('grab_gear_down')
		own.state = logic.KX_STATE1
		crane_head.state = logic.KX_STATE2
		own['crane_arm'] = 0
		own.position[2] = crane_ref.position[2]
	else:
		cont.activate('grab_motion')
		cont.activate('grab_gear_up')
		
def target_ray(cont):
	own = cont.owner
	
	target = cont.sensors['target'].owner
	ship_ray = cont.sensors['ship_ray']

	if ship_ray.positive:
		target.visible = True
		target.position = ship_ray.hitPosition
	else:
		target.visible = False