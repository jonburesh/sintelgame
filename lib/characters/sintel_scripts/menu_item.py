'''
--------------------------------------------------------------------------------------------------------
each menu item has its own script
multiple user script
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main():

	cont = logic.getCurrentController()
	own = cont.owner

	item_selected = cont.sensors['item_selected'].owner
	item_text = cont.sensors['item_text'].owner
	
	item_text.text = own['text']
	
	if own['selected'] == True:
		item_selected.visible = 1
	else:
		item_selected.visible = 0