'''
--------------------------------------------------------------------------------------------------------
saves the .ini file, saves some settings to global dictionary
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render

def save_settings():
	fullscreen_option = logic.getCurrentScene().objects['fullscreen_option']
	post_option = logic.getCurrentScene().objects['post_option']
	ssao_option = logic.getCurrentScene().objects['ssao_option']
	LOD_option = logic.getCurrentScene().objects['LOD_option']
	resolution_option = logic.getCurrentScene().objects['resolution_option']
	difficulty_option = logic.getCurrentScene().objects['difficulty_option']
	ui_scale_option = logic.getCurrentScene().objects['ui_scale_option']
	
	cfg_fullscreen = str(fullscreen_option['option'])
	res = resolution_option['option']
	res = res.split('x')
	cfg_screen_width = str(res[0])
	cfg_screen_height = str(res[1])
	
	print ('Saving config file...')
	#print (cfg_fullscreen, cfg_screen_width, cfg_screen_height)
	set_settings = open('sintel_config.ini', 'w')
	set_settings.write(cfg_screen_width+"\n")
	set_settings.write(cfg_screen_height+"\n")
	set_settings.write(cfg_fullscreen)
	set_settings.close()
	
	logic.globalDict['cfg_post'] = post_option['option']
	logic.globalDict['cfg_ssao'] = ssao_option['option']
	logic.globalDict['cfg_LOD'] = LOD_option['option']
	logic.globalDict['cfg_difficulty'] = difficulty_option['option']
	logic.globalDict['cfg_UI'] = ui_scale_option['option']
	print (logic.globalDict['cfg_difficulty'])
	logic.saveGlobalDict()
	
	render.setWindowSize(int(cfg_screen_width), int(cfg_screen_height)) 