import bge

CONFIG_FOUND = False

def main():

	cont = bge.logic.getCurrentController()
	own = cont.owner

	try:
		config = bge.logic.expandPath("//config.ini")
		print (config)
		loadsettings = open(config, 'r')
		CONFIG_FOUND = True
	except:
		try:
			loadsettings = open('config.ini', 'r')
			CONFIG_FOUND = True
			print (':/')
		except:
			CONFIG_FOUND = False
			print ('Could not locate config.ini')
			
	if CONFIG_FOUND != False:
		gameresolution = loadsettings.readline()
		gameresolution = gameresolution[0:-1]
		gamequal = loadsettings.readline()
		gamequal = gamequal[0:-1]
		glsl = loadsettings.readline()
		glsl = glsl[0:-1]
		
		loadsettings.close()
		
		own['gameresolution'] = gameresolution
		own['gamequal'] = gamequal
		own['GLSL'] = glsl
		
		bge.logic.gameresolution = gameresolution
		bge.logic.gamequal = gamequal
		bge.logic.GLSL = glsl
		
		print ('Loaded Config:',gameresolution, gamequal, 'GLSL:',glsl)