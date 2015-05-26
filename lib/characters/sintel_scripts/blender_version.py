#A quick test to see what blender version is running

def check_version():
	try:
		import Mathutils
		VERSION = 2.49
	except:
		import mathutils
		VERSION = 2.5
	return VERSION