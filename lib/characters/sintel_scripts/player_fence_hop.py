import bge, math

from mathutils import Vector, Matrix
	
def fencehop():
	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	auto_action = cont.sensors['auto_action']
	
	if not auto_action:
		return False
	elif own['isSpaceon']:
		#Gather info on the fence
		fence_obj = auto_action.hitObject
		fence_pos = fence_obj.worldPosition
		
		#get the normal of the fence
		hit_norm = Vector(auto_action.hitNormal)
		hit_norm.z = 0.0
		
		#Vector axis of Sintel
		own_negative_y = Vector(own.getAxisVect((0.0, -1.0, 0.0)))
		own_negative_y.z = 0.0
		
		#Cross it, then get the absolute vaule
		cross = hit_norm.cross(own_negative_y)
		cross = math.fabs(cross[2])
		
		#print (cross)
		
		#Check the angle of approach
		if cross <=.5:
			new_pos = (fence_pos[2] + 2)
			own.worldPosition[2] = new_pos
			
			own['Leaping']=True
			CURRENT_SPEED = own.getLinearVelocity(True)
			
			
			if CURRENT_SPEED[1] < 11:
				CURRENT_SPEED[1] = 11
				
			CURRENT_SPEED[2] = 10
			#print (CURRENT_SPEED)
			own.setLinearVelocity(CURRENT_SPEED ,True)
			own['Tracking']=False
			return True
		else:
			return False
		