'''
--------------------------------------------------------------------------------------------------------
plays a random sound for enemy AI 
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from random import choice

def randSound(sound):
	#sound categories
	growl = ['growl_1','growl_2','growl_3','growl_4','growl_5','growl_6']
	move = ['move_1','move_2']
	attack = ['wood1','wood2','wood3','wood4']
	hurt = ['hurt1','hurt2','hurt3','hurt4']
	death = ['death1','death2','death3','death4']
	#return a random choice from the list, determined by the passed in var
	soundPlay = ''
	if sound =='growl':
		soundPlay = choice(growl)
	elif sound =='move':
		soundPlay = choice(move)
	elif sound =='hurt':
		soundPlay = choice(hurt)
	elif sound =='death':
		soundPlay = choice(death)
	else:
		print ("Unexpected value: %i" % sound)
	return soundPlay