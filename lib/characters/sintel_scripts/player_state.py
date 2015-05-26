import bge

def main():

	cont = bge.logic.getCurrentController()
	own = cont.owner

	cutstate = cont.sensors['cutstate'].positive
	gamestate = cont.sensors['gamestate'].positive

	cutscenestate = cont.actuators['cutscenestate']
	gameplaystate = cont.actuators['gameplaystate']

	if cutstate:
		cont.activate(cutscenestate)
		own.setLinearVelocity([0, 0, 0], True)
		
	if gamestate:
		cont.activate(gameplaystate)
		own.setLinearVelocity([0, 0, 0], True)