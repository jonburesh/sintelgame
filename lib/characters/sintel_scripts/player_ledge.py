import bge

def ledgegrab():

	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	ledge_finder = cont.sensors['ledge_finder']
		
	print ('ledge!')
	ledge = ledge_finder.hitObject
	ledge_pos = ledge.worldPosition
	
	own.worldPosition[1] = (ledge_pos[1] - .5)
	own.worldPosition[2] = (ledge_pos[2] + 3.5)
	
	return