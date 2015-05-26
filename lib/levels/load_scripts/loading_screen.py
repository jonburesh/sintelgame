'''
--------------------------------------------------------------------------------------------------------
will load a level based on the global dictionary value 'Load_Next'
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def load_var():
	try:
		#load global dictionary
		cont.activate(load_dict)
	except:
		print ('no save data')

def main(cont):
	own = cont.owner
	
	LEVEL_MAIN = logic.getCurrentScene().objects['LEVEL_MAIN']
	
	load_file = cont.actuators['load_file']
	load_dict = cont.actuators['load_dict']
	start_docks = cont.actuators['start_docks']
	
	load_var()
	
	try:
		print ('Loading level: '+logic.globalDict['Load_Next'])
		
		#check to see if the there is a backdrop for the currently loading level
		if logic.globalDict['Load_Next'] in logic.getCurrentScene().objects:
			backg = logic.getCurrentScene().objects[logic.globalDict['Load_Next']]
			print (backg)
			backg.position = LEVEL_MAIN.position
		
		#menu is in a different directory from the other levels so we must show it where to look
		if logic.globalDict['Load_Next'] == 'main_menu':
			load_file.fileName = '//..\menu\main_menu.blend'
		#otherwise check in the levels folder
		elif logic.globalDict['Load_Next'] == 'sintel_rig_2':
			load_file.fileName = '//..\characters\sintel_rig_2.blend'
		elif logic.globalDict['Load_Next'] == 'docks_level.blend':
			#load_file.fileName = '//..\characters\sintel_rig_2.blend'
			cont.activate(start_docks)
			print ('DOCKS')
		else:
			if not '.blend' in logic.globalDict['Load_Next']:
				load_file.fileName = '//..\levels\%s.blend' % (logic.globalDict['Load_Next'])
			else:
				load_file.fileName = '//..\levels\%s' % (logic.globalDict['Load_Next'])
			
		#load the file
		cont.activate(load_file)
	except:
		print ('No BGE save file found. Going to main menu.')
		logic.globalDict['Load_Next'] ='main_menu'
		load_file.fileName = '//..\menu\main_menu.blend'
		cont.activate(load_file)