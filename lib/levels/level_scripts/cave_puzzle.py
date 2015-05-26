'''
--------------------------------------------------------------------------------------------------------
script for the cave puzzle
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render
from random import *

ring_1_empty = logic.getCurrentScene().objects['ring_1_empty']
ring_2_empty = logic.getCurrentScene().objects['ring_2_empty']
ring_3_empty = logic.getCurrentScene().objects['ring_3_empty']

def randSound():
	sound_list = ['move_1','move_2','move_3','move_4','move_5','move_1']
	soundPlay = ''
	soundPlay = choice(sound_list)
	return soundPlay

def init():
	render.showMouse(1)

def main():
	cont = logic.getCurrentController()
	own = cont.owner
	
	mouse_over = own.sensors['mouse_over']
	left_click = own.sensors['left_click']
	
	back_glow_point_light = logic.getCurrentScene().objects['back_glow_point_light']
	
	if mouse_over.hitObject != None:
		if left_click.positive:
			OVER = mouse_over.hitObject
			if '1' in OVER:
				rotate('1')
			elif '2' in OVER:
				rotate('2')
			elif '3' in OVER:
				rotate('3')
				
	if ring_1_empty['value'] ==2 and ring_2_empty['value'] == 4 and ring_3_empty['value'] == 7:
		print ('win!')
		cont.activate('set_state')
		cont.activate('add_green')
		back_glow_point_light.state = 2
	
def rotate(ring):
	cont = logic.getCurrentController()
	own = cont.owner
	cont.activate(randSound())
	if ring == '1':
		ring_1_empty['trigger'] = True
		if ring_1_empty['value'] ==7:
			ring_1_empty['value'] = 0
		else:
			ring_1_empty['value'] +=1
	if ring == '2':
		ring_2_empty['trigger'] = True
		if ring_2_empty['value'] ==7:
			ring_2_empty['value'] = 0
		else:
			ring_2_empty['value'] +=1
	if ring == '3':
		ring_3_empty['trigger'] = True
		if ring_3_empty['value'] ==7:
			ring_3_empty['value'] = 0
		else:
			ring_3_empty['value'] +=1