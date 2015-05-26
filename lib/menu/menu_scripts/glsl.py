#Sets the scene to load either the Non GLSL scene or the GLSL scene
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	yes = cont.actuators["yes"]
	no = cont.actuators["no"]

	try:
		loadsettings = open('config.ini', 'r')
	except:
		try:
			print ('looking for config file...')
			loadsettings = open('lib/config.ini', 'r')
		except:
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
	bge.logic.gameresolution = gameresolution
	bge.logic.gamequal = gamequal
	bge.logic.GLSL = glsl

	#Load GLSL?
	if bge.logic.GLSL =='1':
		cont.activate(yes)
		print ('Loaded GLSL game')
	elif bge.logic.GLSL =='0':
		cont.activate(no)
		print ('Loaded Non-GLSL game')
	else:
		print (bge.logic.GLSL)
