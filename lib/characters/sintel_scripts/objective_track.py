# Get the direction to the goal relative to the player, and set the
# compass accordingly
import bge
from mathutils import Matrix

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	tracker = cont.sensors["tracker"].owner
	compass = cont.sensors["sensor"].owner
	playerangle = cont.sensors["once"].owner

	trackerangle = tracker.orientation
	anglematrix = Matrix.Translation(trackerangle[2])

	angle = anglematrix.to_euler()

	rotangle = float(angle[2])


	# Getting the player angle
	playerangle = playerangle.orientation
	playermatrix = Matrix.Translation(playerangle[2])
	
	newplayerangle = playermatrix.to_euler()

	playerrot = float(newplayerangle[2])

	rotangle -= playerrot


	# Converting to radians (damn you, Blender)
	rotangle /= 360.0
	rotangle *= (2 * 3.141592)

	# Setting the angles in radians (which for some absurd reason works
	# despite them being originally given in degrees)
	angle[0] = 3.141 / 2.0
	angle[1] = rotangle
	angle[2] = 0.0


	compass.orientation = angle
	bge.logic.angle = angle
	#print (angle)