#Sets the scene to load either the Non GLSL scene or the GLSL scene
import bge

def main():
	cont = bge.logic.getCurrentController()
	
	own = cont.owner

	yes = cont.actuators["yes"]
	no = cont.actuators["no"]
	
	#Check to see if data is already loaded
	try:
		if bge.logic.globalDict['game_resolution']:
			print ('config data found.')
	except:
		try:
			loadsettings = open('config.ini', 'r')
		except IOError:
			try:
				print(("looking for config file..."))
				loadsettings = open('lib/config.ini', 'r')
			except IOError:
				loadsettings = open('config.ini', 'w+')
				loadsettings.write('1440x900\n')
				loadsettings.write('High\n')
				loadsettings.write('1\n')
		
	gameresolution = loadsettings.readline()
	gameresolution = gameresolution[0:-1]
	gamequal = loadsettings.readline()
	gamequal = gamequal[0:-1]
	glsl = loadsettings.readline()
	glsl = glsl[0:-1]
	loadsettings.close()
	bge.logic.globalDict['game_resolution'] = gameresolution
	bge.logic.globalDict['game_quality'] = gamequal
	bge.logic.globalDict['GLSL'] = glsl

	#Load GLSL?
	if bge.logic.globalDict['GLSL'] =='1':
		cont.activate(yes)
		print( 'Loaded GLSL game')
	elif bge.logic.globalDict['GLSL'] =='0':
		cont.activate(no)
		print( 'Loaded Non-GLSL game')
	else:
		print( bge.logic.globalDict['GLSL'])
