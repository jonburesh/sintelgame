#from math import degrees, acos
from bge import logic 

#test_ob = logic.getCurrentScene().objects['test_ob']
#test_ob2 = logic.getCurrentScene().objects['test_ob.2']

#when idle, rotate feet
def main(cont):
	own = cont.owner
	
	right_foot_ray = cont.sensors['right_foot_ray']	
	right_foot_check = right_foot_ray.owner
	
	left_foot_ray = cont.sensors['left_foot_ray']
	left_foot_check = left_foot_ray.owner

	if right_foot_ray.positive:
		right_pos = right_foot_ray.hitPosition
		right_leg_length = right_foot_check.getDistanceTo(right_pos)
		#test_ob2.worldPosition = [right_pos[0],right_pos[1],right_pos[2]]
		own['right_foot'] = right_leg_length *10
	
		cont.activate('foot_right')
	else:
		cont.deactivate('foot_right')
		
	if left_foot_ray.positive:
		left_pos = left_foot_ray.hitPosition
		left_leg_length = left_foot_check.getDistanceTo(left_pos)
		own['left_foot'] = left_leg_length *10
		#test_ob.worldPosition = [left_pos[0],left_pos[1],left_pos[2]]
		cont.activate('foot_left')
	else:
		cont.deactivate('foot_left')