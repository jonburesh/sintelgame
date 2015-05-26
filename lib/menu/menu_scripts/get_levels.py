'''
--------------------------------------------------------------------------------------------------------
gets a list of the available levels (.blend files)
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import string


#spawn_level = logic.getCurrentScene().objects['spawn_level']
def init():
	global cont, own
	cont = logic.getCurrentController()
	own = cont.owner
	
def gather():
	own['level_count'] =0;
	#levels = logic.getBlendFileList('//')
	#levels = logic.getBlendFileList('//levels')
	levels = logic.getBlendFileList('//../levels')
	#levels += logic.getBlendFileList('//../../../levels')
	
	#levels = dict([(b, None) for b in levels]).keys()
	levels.sort()
	#print (levels)
	#remove non-level blend files
	for file in levels:
		if not '_' in file:
			levels.remove(file)
	logic.globalDict['menu_levels'] = levels
	
def main():
	init()
	gather()
	
	for file in logic.globalDict['menu_levels']:
		own['level_count']+=1
		print ('Found Level:', file)