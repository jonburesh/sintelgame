import os, string, bge

def main():
	try:
		loadsettings = open('config.ini', 'r')
	except:
		try:
			print( 'looking for that config file..')
			loadsettings = open('lib/config.ini', 'r')
		except:
			pass
	resolution = loadsettings.readline()
	resolution = resolution[0:-1]
	loadsettings.close()
	resolution = resolution.split('x')
	print( 'Setting Resolution to', resolution[0] ,'x',resolution[1])
	prog = bge.logic.expandPath("//startup.exe")
	args = [" -f "+str(resolution[0])+' '+str(resolution[1])+" 32 60 -g blender_material = 0 startup.exe"]
	print( os.execvp(prog, (prog,) + tuple(args)))
