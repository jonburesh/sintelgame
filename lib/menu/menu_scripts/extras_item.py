'''
--------------------------------------------------------------------------------------------------------
each extras item has its own script
multiple user script
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import string

def main():

	cont = logic.getCurrentController()
	own = cont.owner

	extras_selected = cont.sensors['extras_selected'].owner
	extras_text = cont.sensors['extras_text'].owner
	
	extras_text.text = own['text']
	
	if own['selected'] == True:
		extras_selected.visible = 1
	else:
		extras_selected.visible = 0