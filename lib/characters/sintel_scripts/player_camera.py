#New camera script
from bge import render as render
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	#Gather sensors + actuators
	mousemove = cont.sensors['mousemove']
	cam = cont.sensors['playercam'].owner
	rightmouse = cont.sensors['rightmouse'].positive
	Ray = cont.sensors["collision"]
	
	#camact = cont.actuators['camact']
	camxrot = cont.actuators['camxrot']
	camyrot = cont.actuators['camyrot']
	lock_cam = cont.actuators['lock_cam']
	lock_cam_track = cont.actuators['lock_cam_track']
	
	Player = bge.logic.getCurrentScene().objects["PlayerCol"]

	#Set mouse pos
	screenwidth = render.getWindowWidth()
	screenheight = render.getWindowHeight()
	
	render.setMousePosition(int(screenwidth/2), int(screenheight/2))
				
	#Rotate camera, but not instantly (bug fix)
	if mousemove.positive and own['wtime']>=.1:
		#Rotate by mouse x + y
		xmouse = (screenwidth/2 - mousemove.position[0]) * own['sensitivity']
		ymouse = (screenheight/2 - mousemove.position[1]) * own['sensitivity']
		#Calculate cam rotation
		#if Player['Fightmode']==True:
			#own['previousx'] = (own['previousx']*.4 + xmouse*.1)
			#own['previousy'] = (own['previousy']*.4 + ymouse*.1)
		#else:
		own['previousx'] = (own['previousx']*.8 + xmouse*.2)
		own['previousy'] = (own['previousy']*.8 + ymouse*.2)
		xmouse = own['previousx']
		ymouse = own['previousy']
		#print (ymouse,xmouse)
		#Set cam rotation
		camyrot.dRot =(ymouse, 0, 0)
		camxrot.dRot =(0, 0, xmouse)
		cont.activate(camxrot)
		cont.activate(camyrot)
	else:
		cont.deactivate(camxrot)
		cont.deactivate(camyrot)
		
	#Something is in the way of the camera
	if Ray.positive:
		Newcampos = Ray.hitPosition
		Newcampos[2] = Newcampos[2] +.2
		cam.position = Newcampos
		OrigCamera = cont.sensors["campos"].owner
		cam.worldOrientation = OrigCamera.worldOrientation
	else:
		OrigCamera = cont.sensors["campos"].owner
		cam.position = OrigCamera.position
	if Player['Locked'] ==False:
		cam.worldOrientation = OrigCamera.worldOrientation 

	#Camera trick - Thanks to YoFrankie
	old_lens = cam.lens	
	if cam['run']==True or Player['Locked'] ==True:
		lens = 28
	if cam['run']==False and Player['Locked'] ==False:
		lens = 35
		
	if lens != old_lens:
		cam.lens = (lens*0.04) + (old_lens*0.96)
	
	#BATTLE CAM
	if Player['Locked'] ==True:
		cont.activate(lock_cam)
		try:
			lock_cam_track.object = Player['Target']
			cont.activate(lock_cam_track)
		except:
			pass
	else:
		cont.deactivate(lock_cam)
		cont.deactivate(lock_cam_track)