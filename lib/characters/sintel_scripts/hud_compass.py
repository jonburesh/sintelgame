#Simple script for chaning the compass
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	norm = cont.actuators["norm"]
	warn = cont.actuators["warn"]
	dang = cont.actuators["dang"]

	if bge.logic.Alert ==1:
		cont.activate(norm)
	if bge.logic.Alert ==2:
		cont.activate(warn)
	if bge.logic.Alert >=3:
		cont.activate(dang)