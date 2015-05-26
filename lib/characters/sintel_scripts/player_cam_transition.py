'''
--------------------------------------------------------------------------------------------------------
Translates the current camera to player cam - currently broken
getting orientation should be easy but it gets the inverse of what I need and inverting the matrix 
is spitting out an error
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render
import mathutils

sintel = logic.getCurrentScene().objects['sintel_col']
player_cam = logic.getCurrentScene().objects['player_camera']
sintel_cam_target = logic.getCurrentScene().objects['sintel_cam_target']
cam_defualt_pos = logic.getCurrentScene().objects['cam_defualt_pos']
#test_cam = logic.getCurrentScene().objects['test_cam']

slerp_factor = 0.0

scene = logic.getCurrentScene()

def init(cont):
	global from_quat, to_quat
	own = cont.owner
	
	current_cam = scene.active_camera
	#distance between player camera and the tracker
	dist = (own.position - player_cam.position)
	#set us at the proper position + orientation
	own.worldPosition = current_cam.worldPosition + dist
	own.localOrientation = current_cam.localOrientation.invert() # <------ doesn't work. can't explain that
	#where we are coming from
	from_matrix = own.worldOrientation.copy()
	from_quat = from_matrix.to_quaternion()
	#where we are going 
	to_mat = cam_defualt_pos.worldOrientation
	to_quat = to_mat.to_quaternion()
	#set camera and go!
	player_cam.lens = current_cam.lens
	scene.active_camera = player_cam
	own.state = logic.KX_STATE2

def main(cont):
	global dest, from_quat, slerp_factor, to_quat
	own = cont.owner
	#where we are going
	dest = cam_defualt_pos.worldPosition.copy()
	diff = dest - own.worldPosition.copy()
	#lerping
	if diff.magnitude > 0.1:
		 diff *= 0.025

	if slerp_factor < 1.0:
		slerp_factor += 0.005
		#print ('slerp', slerp_factor)
	
	own.worldPosition += diff
	#slerping rotation
	quatInterpolation = from_quat.slerp(to_quat, slerp_factor)
	own.worldOrientation = quatInterpolation.to_matrix()
	#reached our destination
	if own.worldPosition == dest:
		#own.orientation = cam_defualt_pos.orientation
		logic.sendMessage('player_unfreeze')
		logic.sendMessage('HUD_on')
		render.setMousePosition(int(render.getWindowWidth() / 2), int(render.getWindowHeight() / 2))
		own.state = logic.KX_STATE1