'''
--------------------------------------------------------------------------------------------------------
each level item has its own script
multiple user script
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import string

def main():

	cont = logic.getCurrentController()
	own = cont.owner

	level_text = cont.sensors['level_text'].owner
	level_selected = cont.sensors['level_selected'].owner
	
	level_text.text = own['text']
	
	if own['selected'] == True:
		level_selected.visible = 1
	else:
		level_selected.visible = 0