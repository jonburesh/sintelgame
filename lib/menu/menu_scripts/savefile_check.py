import bge

def main():

	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	Resumebut = cont.sensors["resume"].owner
	load_dict = cont.actuators['load_dict']
	
	cont.activate(load_dict)
	try:
		if bge.logic.globalDict['level_name']:
			if bge.logic.globalDict['level_name'] != 'default':
				Resumebut['save']=True
				own['resume']=True
				Resumebut['level_next']=bge.logic.globalDict['level_name']
				#print (Resumebut['level_next'])
	except:
		print ('No save file could be found.')
		own['resume']=False
		Resumebut['save']=False
