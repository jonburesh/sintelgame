from bge import logic
from random import *

def RanSounds(type):
	grass = ['foot_grass_1', 'foot_grass_2', 'foot_grass_3', 'foot_grass_4', 'foot_grass_5', 'foot_grass_6', 'foot_grass_7', 'foot_grass_8', 'foot_grass_9', 'foot_grass_10', 'foot_grass_11', 'foot_grass_12', 'foot_grass_13']
	wood = ['wood1','wood2','wood3','wood4']
	action = ''
	if type ==1:
		action = choice(grass)
	elif type ==2:
		action = choice(wood)
	else:
		print ("Unexpected value: %i" % type)
	return action

def main():
	foots = logic.getCurrentScene().objects['player_footprints']
	
	cont = logic.getCurrentController()
	own = cont.owner
	if own['MOVING'] and not own['DREAM']:
		if own['RUNNING']:
			if foots['foot_timer'] >= .4:
				cont.activate(RanSounds(1))
				foots['foot_timer'] = 0
		else:
			if foots['foot_timer'] >= .55:
				cont.activate(RanSounds(1))
				foots['foot_timer'] = 0