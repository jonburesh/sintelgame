'''
--------------------------------------------------------------------------------------------------------
sets what level to load next
uses message sensor with subject level_next
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main():
	cont = logic.getCurrentController()
	own = cont.owner
	
	# recived the level to load message
	level_mess = cont.sensors['level_mess']

	#Has to load before it saves or else it will overwrite.
	try:
		logic.loadGlobalDict()
	except:
		pass
	#print (bge.logic.globalDict.keys())
	
	if level_mess.positive:
		#print (level_mess.bodies[0])
		logic.globalDict['Load_Next'] = level_mess.bodies[0]
		print ('will load ',logic.globalDict['Load_Next'], 'next.')
		logic.saveGlobalDict()

		#print ('No save file found, creating one.')