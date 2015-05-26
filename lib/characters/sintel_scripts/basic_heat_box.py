import bge
burnObjStr = "Torch_Fire_emitter"
def main(cont):
	own = cont.owner
	if 'Rp' not in own:
		startup(own)
	if own["timer"] > 5:
		caster(own)
		
	if own["timer"] > 8:
		own.endObject()		


def caster(own):	
	for i in range(6):
		bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition = own.worldPosition 	
		if i == 1:
			bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition.x = own.worldPosition.x + 10 #pos x
			
		if i == 2:
			bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition.x = own.worldPosition.x - 10 #neg x
			
		if i == 3:
			bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition.y = own.worldPosition.y + 10 #pos y
			
		if i == 4:
			bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition.y = own.worldPosition.y - 10 #neg y		

		if i == 5:
			bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition.z = own.worldPosition.z + 10 #pos z
			
		if i == 6:
			bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition.z = own.worldPosition.z - 10 #neg z	
			
			 			
		ray_info = own.rayCast(own,(bge.logic.getCurrentScene().objects["Ray_pusher"]),100,"Flammable")
		#bge.render.drawLine(own.worldPosition,(bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition),(1,1,1)) # debug only can be deleted 
		if ray_info[0] != None:
			print(ray_info[0])
			bge.logic.getCurrentScene().objects[burnObjStr]["hotObjs"].append(ray_info[0])
			del (bge.logic.getCurrentScene().objects[str(ray_info[0])]['Flammable'])
		
		

		
def startup(own):
	own["Rp"] = 0
	bge.logic.getCurrentScene().addObject("Ray_pusher",own,0)
	
	
	
	
	
#			if 'Flammable' in bge.logic.getCurrentScene().objects[str(own["colHolder"])]: # check if the collition object has the prop flammable 
#				if own["colHolder"]not in bge.logic.getCurrentScene().objects[burnObjStr]["hotObjs"]: # checks that the new object to be burnt is not already in a list of objects to be burnt 
#					bge.logic.getCurrentScene().objects[burnObjStr]["hotObjs"].append(own["colHolder"])# appends the new object to the list of objects to be burnt 
#					print(bge.logic.getCurrentScene().objects[burnObjStr]["hotObjs"])#temp
#					del (bge.logic.getCurrentScene().objects[str(own["colHolder"])]['Flammable']) # deletes the flammable prop from the object to prevent double burning
#					
