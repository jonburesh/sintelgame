#Based off Yo Frankie idea
#Cheers to them

#Used to keep the player from going through walls + buildings)

import bge

from mathutils import Vector, Matrix

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	wall_ray = cont.sensors["wall_ray"]

	wall_normal = Vector(wall_ray.hitNormal)
	wall_normal.z = 0.0

	own_negative_y = Vector(own.getAxisVect((0.0, -1.0, 0.0)))
	own_negative_y.z = 0.0
				
	cross = wall_normal.cross(own_negative_y)

	if cross.z > 0.0:
		new_dir = Matrix.Rotation(-90.0, 3, 'X') * wall_normal
	else:
		new_dir = Matrix.Rotation(90.0, 3, 'X') * wall_normal
	
	#print (new_dir)
	#own.alignAxisToVect(new_dir, 0, .1)