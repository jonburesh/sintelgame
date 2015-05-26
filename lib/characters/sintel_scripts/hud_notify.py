#Creates a new notification and places it in the proper position
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	notetext = cont.sensors['notetext']
	addnote = cont.actuators['addnote']

	if notetext.positive and bge.logic.Hide ==False:
		own['notify']+=1
		cont.activate(addnote)
		own['note'] = notetext.bodies[0]
		own['time']=0

	if own['notify']>5 or own['time']>=7:
		own['notify']=1
		own['time']=0
