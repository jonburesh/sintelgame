#looks for and returns the current level name as defined by the LEVEL_MAIN object ('level_name' property)
import bge

def main():
	scene = bge.logic.getCurrentScene()
	try: 
		level_main = scene.objects["LEVEL_MAIN"]
		print ('found LEVEL_MAIN')
		try:
			level_name = level_main['level_name']
			print ('level is '+level_name)
			return level_name
		except:
			print ('LEVEL_MAIN has no property "level_name"')
			return False
	except:
		print ('Object LEVEL_MAIN could not be found.')
		return False