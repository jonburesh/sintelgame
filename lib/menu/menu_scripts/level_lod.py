#Only for use if sintel is not linked in (Menu Scene)
import math, bge

def checkconfig():
	try:
		loadsettings = open('config.ini', 'r')
	except:
		try:
			print ('looking for config file...')
			loadsettings = open('lib/config.ini', 'r')
		except:
			pass
	gameresolution = loadsettings.readline()
	gameresolution = gameresolution[0:-1]
	gamequal = loadsettings.readline()
	gamequal = gamequal[0:-1]
	loadsettings.close()
	bge.logic.QUAL = gamequal
	print ('Global quality set to', gamequal)
	
def main():
	scene = bge.logic.getCurrentScene()
	cam = bge.logic.getCurrentScene().active_camera
	cont = bge.logic.getCurrentController()
	own = cont.owner

	if own['obtainlist']==False:
		checkconfig()
		bge.logic.objlist = []
		for obj in scene.objects:
			if "lod" in obj:
				bge.logic.objlist.append(obj)
				own['obtainlist']=True
				#print (bge.logic.objlist)
	else:
		for obj in bge.logic.objlist:
			depth = obj.position[0]*cam.world_to_camera[2][0] + obj.position[1]*cam.world_to_camera[2][1] + obj.position[2]*cam.world_to_camera[2][2] + cam.world_to_camera[2][3]
			depth = abs(depth)
			try:
				if bge.logic.QUAL =='High':
					if depth < own['firstlod']:
						obj['lod']=0
					if depth >= own['firstlod']:
						obj['lod']=1
					if depth >= own['2ndlod']:
						obj['lod']=2
					#if not (cam.pointInsideFrustum(obj.position)):
						#obj['lod']=2
				elif bge.logic.QUAL =='Low':
					if depth < own['firstlod']:
						obj['lod']=1
					if depth >= own['firstlod']:
						obj['lod']=2
					if depth >= own['2ndlod']:
						obj['lod']=2
					#if not (cam.pointInsideFrustum(obj.position)):
						#obj['lod']=2
			except:
				bge.logic.QUAL = 'High'
