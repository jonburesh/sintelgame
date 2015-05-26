from bge import logic
from mathutils import Vector

def main():
	cont = logic.getCurrentController()
	own = cont.owner

	cart_pos = logic.getCurrentScene().objects['cart_pos']
	player = logic.getCurrentScene().objects['sintel_col']

	own.setParent(cart_pos)
	
	own.worldPosition = cart_pos.worldPosition
	own.worldOrientation = cart_pos.worldOrientation
	#body.worldOrientation = cart_pos.worldOrientation
	
	from_pos = own.position
	
	to_pos = from_pos[:]
	to_pos = [from_pos[0], from_pos[1], (from_pos[2] - 150)]

	floor_ray = own.rayCast(to_pos, from_pos, 0, "ground")
	
	if floor_ray[2]:
		own.alignAxisToVect(floor_ray[2], 2, .1)