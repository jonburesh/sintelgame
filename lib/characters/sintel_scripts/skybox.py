#Gets the position and rotation of the camera for a skybox
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	isskybox = cont.sensors['isskybox'].positive
	addskybox = cont.actuators['addskybox']

	#If this level has Dynamic Skybox enabled
	if isskybox:
		if own['Skybox']==False:
			own['Skybox']=True
		else:
			print ('Dynamic Skybox is already enabled for this level.')

	if own['Skybox']==True:
		#Get the rotation and position
		bge.logic.skyboxcamrot = own.worldOrientation
		bge.logic.skyboxcampos = own.worldPosition
		bge.logic.skyboxcamlens = own.lens
		#Add the skybox scene
		if own['addedsb']==False:
			try:
				addskybox.scene = 'Skybox'
				cont.activate(addskybox)
				own['addedsb']=True
			except:
				print ('Skybox scene not found. Make sure it is called "Skybox"')