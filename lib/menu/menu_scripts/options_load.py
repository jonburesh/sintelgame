'''
--------------------------------------------------------------------------------------------------------
loads the .ini file and sets options values, also loads some settings from global dict
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main():

	#defualt
	cfg_screen_width = '1024'
	cfg_screen_height = '768'
	cfg_fullscreen = 'True'
	
	fullscreen_option = logic.getCurrentScene().objects['fullscreen_option']
	post_option = logic.getCurrentScene().objects['post_option']
	ssao_option = logic.getCurrentScene().objects['ssao_option']
	LOD_option = logic.getCurrentScene().objects['LOD_option']
	resolution_option = logic.getCurrentScene().objects['resolution_option']
	difficulty_option = logic.getCurrentScene().objects['difficulty_option']
	ui_scale_option = logic.getCurrentScene().objects['ui_scale_option']
	
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
		print ('Loaded settings:', cfg_screen_width, cfg_screen_height, cfg_fullscreen)
	except:
		print ('Creating config file')
		set_settings = open('sintel_config.ini', 'w')
		set_settings.write(cfg_screen_width+"\n")
		set_settings.write(cfg_screen_height+"\n")
		set_settings.write(cfg_fullscreen)
		set_settings.close()
		
	try:
		logic.loadGlobalDict()
		post_option['option'] = logic.globalDict['cfg_post']
		ssao_option['option'] = logic.globalDict['cfg_ssao']
		LOD_option['option'] = logic.globalDict['cfg_LOD']
		difficulty_option['option'] = logic.globalDict['cfg_difficulty']
		ui_scale_option['option'] = logic.globalDict['cfg_UI']
	except:
		print ('Saving Global Dict')
		logic.globalDict['cfg_post'] = True
		logic.globalDict['cfg_LOD'] = 'High'
		logic.globalDict['cfg_difficulty'] = 'Easy'
		logic.globalDict['cfg_UI'] = 'Normal'
		logic.saveGlobalDict()
		
	if cfg_fullscreen == 'True':
		fullscreen_option['option'] = True
	else:
		fullscreen_option['option'] = False
	
	resolution_option['option'] = cfg_screen_width+'x'+cfg_screen_height