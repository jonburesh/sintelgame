import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	# recived the level to load message
	level_mess = cont.sensors['level_mess']

	#Has to load before it saves or else it will overwrite.
	bge.logic.loadGlobalDict()
	#print (bge.logic.globalDict.keys())
	
	if level_mess.positive:
		#print (level_mess.bodies[0])
		bge.logic.globalDict['Load_Next'] = level_mess.bodies[0]
		print ('will load ',bge.logic.globalDict['Load_Next'], 'next.')
		bge.logic.saveGlobalDict()

		#print ('No save file found, creating one.')