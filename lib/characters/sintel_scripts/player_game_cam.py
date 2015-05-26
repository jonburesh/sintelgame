'''
--------------------------------------------------------------------------------------------------------
standard player camera system
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render
import mathutils

cont = logic.getCurrentController()
own = cont.owner

mouse_move = cont.sensors['mouse_move']
cam_col_check = cont.sensors["cam_col_check"]
#player_cam_pos = cont.sensors["player_cam_pos"].owner
player_camera = cont.sensors["player_camera"].owner
sintel_col = logic.getCurrentScene().objects['sintel_col']
player_camera = logic.getCurrentScene().objects['player_camera']
cam_col = logic.getCurrentScene().objects['cam_col_check']

cam_x_rot = cont.actuators['cam_x_rot']
cam_y_rot = cont.actuators['cam_y_rot']
set_parent = cont.actuators['set_parent']
remove_parent = cont.actuators['remove_parent']

SENSITIVITY = .001
MARGIN = 2

def main():
	#get screen size
	screen_width = render.getWindowWidth()
	screen_height = render.getWindowHeight()
	#center the mouse
	render.setMousePosition(int(screen_width/2), int(screen_height/2))
	#if mouse is moving
	if mouse_move.positive:
		
		x_mouse = (screen_width / 2 - mouse_move.position[0]) * own['SENSITIVITY']
		y_mouse = (screen_height / 2 - mouse_move.position[1]) * own['SENSITIVITY']
		
		own['previous_x'] = (own['previous_x'] * .8 + x_mouse * .2)
		own['previous_y'] = (own['previous_y'] * .8 + y_mouse * .2)
		#limit camera rotation
		cam_angle = own.localOrientation.to_euler()
		#print (cam_angle)
		#cam_angle[0] = max(min(cam_angle[0], 0), 3)
		cam_angle.to_matrix()
		own.localOrientation = cam_angle
		#move the camera
		cam_x_rot.dRot =(0, 0, x_mouse)
		cam_y_rot.dRot =(y_mouse, 0, 0)
			
		cont.activate(cam_x_rot)
		cont.activate(cam_y_rot)
	else:
		cont.deactivate(cam_x_rot)
		cont.deactivate(cam_y_rot)
		
	#camera lense transition - thanks to YoFrankie
	old_lens = player_camera.lens	
	if sintel_col['RUNNING']==True and sintel_col['MOVING'] ==True:
		lens = 22
		own['SENSITIVITY'] = .00075
	if sintel_col['RUNNING']==True and sintel_col['MOVING'] ==False:
		lens = 35
		own['SENSITIVITY'] = .001
	if sintel_col['RUNNING']==False:
		lens = 35
		own['SENSITIVITY'] = .001
	if lens != old_lens:
		player_camera.lens = (lens*0.02) + (old_lens*0.98)
	
	#camera collision
	if cam_col_check.positive:
		player_camera.worldPosition = cam_col_check.hitPosition
		player_camera.localPosition.y += MARGIN
	else:
		player_camera.worldPosition = cam_col.worldPosition
		player_camera.localPosition.y -= cam_col_check.range - MARGIN