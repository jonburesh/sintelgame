'''
--------------------------------------------------------------------------------------------------------
each options item has its own script
multiple user script
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import string

def main():

	cont = logic.getCurrentController()
	own = cont.owner

	options_selected = cont.sensors['options_selected'].owner
	options_text = cont.sensors['options_text'].owner
	options_option = cont.sensors['options_option'].owner
	
	options_text.text = own['text']
	options_option.text = str(own['option'])
	
	if own['selected'] == True:
		options_selected.visible = 1
	else:
		options_selected.visible = 0