'''
--------------------------------------------------------------------------------------------------------
freezes the player
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

sintel = logic.getCurrentScene().objects['sintel_col']
sintel_rig = logic.getCurrentScene().objects['sintel_rig']
sintel_cam_target = logic.getCurrentScene().objects['sintel_cam_target']
cam_defualt_pos = logic.getCurrentScene().objects['cam_defualt_pos']

def main(cont):
	own = cont.owner
	own.setLinearVelocity([0, 0, 0], True)
	
	own['FORWARD'] = False
	own['LEFT'] = False
	own['RIGHT'] = False
	own['BACK'] = False
	own['MOVE'] = False
	own['RUNNING'] = False
	own['RUN'] = False
	
	own['SPEED'] = 0
	own['RUN_SPEED'] = 0
	
	sintel_rig.playAction('sintel_idle_no_feet', 30, 219, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = 1, blendin = 10)

def unfreeze(cont):
	print ('unfreezing player')
	sintel.state = logic.KX_STATE1
	sintel_cam_target.state = logic.KX_STATE1
	sintel_cam_target.orientation = cam_defualt_pos.orientation
	

def freeze(cont):
	print ('freezing player')
	sintel_cam_target.orientation = cam_defualt_pos.orientation
	sintel.state = logic.KX_STATE16