'''
--------------------------------------------------------------------------------------------------------
makes sure we stay on the floor, rotated the right way
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render
from mathutils import *
from math import *

def main(cont):
	own = cont.owner
	Stiff = 500
	Damping = 500


	p0 = own.localPosition
	p1 = p0 - own.worldOrientation*Vector((0.0,0.0,own['hover_height']))

	obj, point, normal = own.rayCast(p1, None, 0, 'ground')

	Vel = own.getLinearVelocity(False)
	
	if obj:
		#render.drawLine(point, own.worldPosition, [0.0,0.0,1.0])
		Loc1 = point
		Loc2 = own.worldPosition


		L = (Loc2-Loc1)
		Length = L.length

		V = (Vel).dot(L)/Length

		ForceSpring =((Length-own['hover_height'])**(3))*Stiff
		ForceDamper = Damping*V
		Force = L/Length*(ForceSpring+ForceDamper)
		
		mmat = own.worldOrientation.copy()


		own.applyForce(-Force+normal, False)
			
		own.alignAxisToVect(normal, 2,0.5)