from bge import render as render
import bge

def main():
	render.showMouse(0)

	cont = bge.logic.getCurrentController()
	own = cont.owner

	resume = cont.actuators['resume']
	resume.scene = 'Scene'
	
	cont.activate(resume)
