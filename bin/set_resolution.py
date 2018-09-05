'''
--------------------------------------------------------------------------------------------------------
run the game, load screen settings and such
uses an .ini file for screen settings will use globalDict for all other data
--------------------------------------------------------------------------------------------------------
'''
import os, string
from bge import logic, render

def main():
	cont = logic.getCurrentController()
	own = cont.owner
	
	#defualt settings
	#cfg_screen_width = '1024'
	#cfg_screen_height = '768'
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
		
		render.setWindowSize(int(cfg_screen_width), int(cfg_screen_height))
		
	except:
		print ('Creating config file')
		
		cfg_screen_width = render.getWindowWidth()
		cfg_screen_height = render.getWindowHeight()
		
		set_settings = open('sintel_config.ini', 'w')
		set_settings.write(str(cfg_screen_width)+"\n")
		set_settings.write(str(cfg_screen_height)+"\n")
		set_settings.write(cfg_fullscreen)
		set_settings.close()
		
	cont.activate('start_game')
	#print (cfg_fullscreen)