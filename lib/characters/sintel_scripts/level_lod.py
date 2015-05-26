import math, bge
'''
def checkconfig():
	try:
		loadsettings = open('config.ini', 'r')
	except:
		try:
			print ('looking for config file...')
			loadsettings = open('lib/config.ini', 'r')
		except:
			pass
	try:
		gameresolution = loadsettings.readline()
		gameresolution = gameresolution[0:-1]
		gamequal = loadsettings.readline()
		gamequal = gamequal[0:-1]
		loadsettings.close()
		bge.logic.QUAL = gamequal
		print ('Global quality set to', gamequal)
	except:
		print ('could not load config file')
		bge.logic.QUAL = 'High'
		print ('Global quality set to', bge.logic.QUAL)
'''	
def main():
	scene = bge.logic.getCurrentScene()
	cam = bge.logic.getCurrentScene().active_camera
	cont = bge.logic.getCurrentController()
	own = cont.owner

	if own['obtainlist']==False:
		#checkconfig()
		bge.logic.objlist = []
		for obj in scene.objects:
			if "lod" in obj:
				bge.logic.objlist.append(obj)
				own['obtainlist']=True
			else:
				own['obtainlist']=True
		if bge.logic.objlist ==[]:
			print ('no lod props found')
	else:
		for obj in bge.logic.objlist:
			campos = cam.worldPosition
			objpos = obj.worldPosition
			disx = objpos[0] - campos[0]
			disy = objpos[1] - campos[1]
			disz = objpos[2] - campos[2]
			depth = (disx * disx) + (disy * disy) + (disz * disz)
			depth = abs(depth)
			#print (obj,depth)
			try:
				if bge.logic.QUAL =='High':
					if depth < 50000:
						obj['lod']=0
					if depth >= 75000:
						obj['lod']=1
					if depth >= 100000:
						obj['lod']=2
						obj.setVisible(1)
					elif depth >= 700000:
						obj.setVisible(0)
					#if not (cam.pointInsideFrustum(obj.position)):
						#obj['lod']=2
				elif bge.logic.QUAL =='Low':
					if depth < 25000:
						obj['lod']=0
					if depth >= 50000:
						obj['lod']=1
					if depth >= 75000:
						obj['lod']=2
						obj.setVisible(1)
					elif depth >= 100000:
						obj.setVisible(0)
					#if not (cam.pointInsideFrustum(obj.position)):
						#obj['lod']=2
			except:
				bge.logic.QUAL = 'Low'
