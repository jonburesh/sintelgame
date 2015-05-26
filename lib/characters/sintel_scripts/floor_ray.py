'''
--------------------------------------------------------------------------------------------------------
sets sintel's orientation based on the hitnormal of the ground
this is for going up + down hills smoothly
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from mathutils import Vector
import math

cont = logic.getCurrentController()
own = cont.owner

def main():
	if own['MOVE']:
		from_pos = own.position

		to_pos = from_pos[:]
		to_pos = [from_pos[0], from_pos[1], (from_pos[2] - 100)]

		floor_ray = own.rayCast(to_pos, from_pos, 0, "ground")
			
		if floor_ray[1]:
			own.alignAxisToVect(floor_ray[2], 2, 0.1)
			
		if floor_ray[2] != None:
		
			var = math.acos(floor_ray[2][2])
			var = (var * 180) / 3.14
			own['floor_angle'] = var
		#print (var)