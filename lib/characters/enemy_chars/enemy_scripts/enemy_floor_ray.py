'''
--------------------------------------------------------------------------------------------------------
makes sure we stay on the floor, rotated the right way
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from mathutils import Vector

cont = logic.getCurrentController()
own = cont.owner

def main():
	from_pos = own.position

	to_pos = from_pos[:]
	to_pos = [from_pos[0], from_pos[1], (from_pos[2] -5)]

	floor_ray = own.rayCast(to_pos, from_pos, 0, "ground")
			
	if floor_ray[1]:
		own.alignAxisToVect(floor_ray[2], 2, .1)