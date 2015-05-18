#Overcomplicated but it works :)

def main():
	try:
		loadsettings = open('config.ini', 'r')
	except:
		try:
			print( 'looking for config file...')
			loadsettings = open('lib/config.ini', 'r')
		except:
			pass
	gameresolution = loadsettings.readline()
	gameresolution = gameresolution[0:-1]
	gamequal = loadsettings.readline()
	gamequal = gamequal[0:-1]
	glsl = loadsettings.readline()
	glsl = glsl[0:-1]
	loadsettings.close()

	try:
		loadsettings = open('config.ini', 'w')
	except:
		try:
			print( 'looking for config file...')
			loadsettings = open('lib/config.ini', 'w')
		except:
			pass
	loadsettings.write(gameresolution+"\n")
	loadsettings.write(gamequal+"\n")
	loadsettings.write('0'+"\n")
	loadsettings.close()
