'''
--------------------------------------------------------------------------------------------------------
plays a random sound for sintel
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from random import choice

def randSound(sound):
	#sound categories
	attack = ['wood_hit1']
	#return a random choice from the list, determined by the passed in var
	soundPlay = ''
	if sound =='attack':
		soundPlay = choice(attack)
	else:
		print ("Unexpected value: %i" % sound)
	return soundPlay