'''
--------------------------------------------------------------------------------------------------------
run the game, load screen settings and such
uses an .ini file for screen settings will use globalDict for all other data
--------------------------------------------------------------------------------------------------------
'''
import os, string
from bge import logic

def main():

	#defualt settings
	cfg_screen_width = '1024'
	cfg_screen_height = '768'
	cfg_fullscreen = 'True'

	try:
		load_settings = open('sintel_config.ini', 'r')
		#load screen width
		cfg_screen_width = load_settings.readline()
		cfg_screen_width = cfg_screen_width[0:-1]
		#screen height
		cfg_screen_height = load_settings.readline()
		cfg_screen_height = cfg_screen_height[0:-1]
		#fullscreen option
		cfg_fullscreen = load_settings.readline()
		cfg_fullscreen = cfg_fullscreen
		load_settings.close()
		print ('loaded properly', cfg_fullscreen)
		
	except:
		pass

	prog = logic.expandPath("//sintel_linux")
	
	if cfg_fullscreen == 'True':
		args = [" -f -c sintel_linux"]
	else:
		args = [" -w -c sintel_linux"]
			
	print( os.execvp(prog, (prog,) + tuple(args)))
