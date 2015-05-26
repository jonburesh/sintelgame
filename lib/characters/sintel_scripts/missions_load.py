import string, bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	des = cont.sensors['des'].owner
	des2 = cont.sensors['des2'].owner
	des3 = cont.sensors['des3'].owner
	title = cont.sensors['title'].owner

	own['id'] =bge.logic.MissionID
	own['title'] = bge.logic.MissionTitle
	own['discript'] = bge.logic.MissionDiscription
	own['skip'] = bge.logic.MissionSkipable

	#own['']

	des['Text'] = own['discript']
	title['Text'] = own['title']
