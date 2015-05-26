#Deals with objectives and cutscenes
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner
	#NEEDS TO BE RE-WRITTEN
	try:
		O1 = bge.logic.getCurrentScene().objects["objective1"]
		own['foundobje'] =1
	except:
		#print ('No objective points found.')
		own['objective']=False
		own['foundobje'] =0
	try:
		O2 = bge.logic.getCurrentScene().objects["objective2"]
		own['foundobje'] =2
	except:
		#print ('Only one objective point found.')
		pass
	try:
		O3 = bge.logic.getCurrentScene().objects["objective3"]
		own['foundobje'] =3
	except:
		pass

	if own['objective']==True:
		if own['id']==1:
			try:
				own.worldOrientation = O1.worldOrientation
				own.worldPosition = O1.worldPosition
			except:
				print ('No objective points found; Turing off objective tracker')
				own['objective']=False
		if own['id']==2:
			try:
				own.worldOrientation = O2.worldOrientation
				own.worldPosition = O2.worldPosition
			except:
				#print ('Only one objective point was found...')
				own['objective']=False
		if own['id']==3:
			try:
				own.worldOrientation = O3.worldOrientation
				own.worldPosition = O3.worldPosition
			except:
				#print ('Only two objective points were found.')
				own['objective']=False

		notify = cont.actuators['notify']
		Player = bge.logic.getCurrentScene().objects["PlayerCol"]
		distance = own.getDistanceTo(Player)
		if distance <= own['range']:
			if own['id']<=own['foundobje']:
				own['id']+=1
				cont.activate(notify)
			else:
				own['objective']=False