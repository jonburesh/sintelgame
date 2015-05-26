import bge

def main():

	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	music = cont.actuators["Music"]
	music.stopSound()
	
	print ('stopping sound')