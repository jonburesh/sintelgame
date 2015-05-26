import bge

def main():

	cont = bge.logic.getCurrentController()
	own = cont.owner

	backspot = cont.sensors["backspot"].owner
	handspot = cont.sensors["handspot"].owner
	
	cloth_movement = cont.actuators['cloth_movement']

	if own['etime']==6 and own['equip']==True:
		cont.activate(cloth_movement)
		
	if own['etime']==11 and own['equip']==True:
		own.worldPosition = backspot.worldPosition
		own.worldOrientation = backspot.worldOrientation
		
	if own['etime']==12 and own['equip']==True:
		own.worldPosition = handspot.worldPosition
		own.worldOrientation = handspot.worldOrientation